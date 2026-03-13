from .model_loader import load_model
import torch
import numpy as np
from PIL import Image
import io

MODEL_PATH = "models/chest_xray_model.pth"

model = load_model(MODEL_PATH)

DISEASES = [
    "Atelectasis", "Cardiomegaly", "Effusion", "Infiltration",
    "Mass", "Nodule", "Pneumonia", "Pneumothorax",
    "Consolidation", "Edema", "Emphysema", "Fibrosis",
    "Pleural_Thickening", "Hernia"
]

def preprocess_image(file):

    img_bytes = file.file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert("L")
    img = img.resize((224,224))
    img = np.array(img, dtype=np.float32)/255.0
    img = np.expand_dims(img, axis=0)  # batch dimension
    img = np.expand_dims(img, axis=0)  # channel dimension
    tensor = torch.tensor(img, dtype=torch.float32)
    return tensor

def predict_xray(file):

    tensor = preprocess_image(file)

    with torch.no_grad():

        output = model(tensor)
        probs = torch.sigmoid(output).numpy()[0]

    # بناء قائمة الأمراض مع نسبة الثقة
    results = []
    for i, disease in enumerate(DISEASES):
        results.append({
            "disease": disease,
            "confidence": float(probs[i])
        })

    # ترتيب النتائج حسب الثقة
    results = sorted(results, key=lambda x: x["confidence"], reverse=True)

    return {
        "diagnosis": results
    }