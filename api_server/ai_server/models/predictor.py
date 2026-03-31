import torch 
import numpy as np
from PIL import Image
import io
from transformers import AutoImageProcessor, AutoModelForImageClassification

HF_MODEL_NAME = "RoccoCristian/Chest-Xray-Classification"

# تحميل معالج الصور والنموذج من هاجنغ فيس
processor = AutoImageProcessor.from_pretrained(HF_MODEL_NAME)
model = AutoModelForImageClassification.from_pretrained(HF_MODEL_NAME)

# استخراج قائمة الأمراض من إعدادات النموذج
DISEASES = [model.config.id2label[i] for i in range(len(model.config.id2label))]

def preprocess_image(file):
    img_bytes = file.file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    # معالجة الصورة لتتناسب مع النموذج
    inputs = processor(images=img, return_tensors="pt")
    return inputs

def predict_xray(file):
    inputs = preprocess_image(file)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=1).numpy()[0]  # النهج المعتاد للنواتج التصنيفية

    # بناء قائمة الأمراض مع نسبة الثقة
    results = []
    for i, disease in enumerate(DISEASES):
        confidence = float(probs[i]) if i < len(probs) else 0.0
        results.append({
            "disease": disease,
            "confidence": confidence
        })

    # ترتيب النتائج حسب الثقة
    results = sorted(results, key=lambda x: x["confidence"], reverse=True)

    return {
        "diagnosis": results
    }