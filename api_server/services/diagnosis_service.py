from api_server.schemas.diagnosis_schema import DiagnosisResult, DiseaseConfidence
import random

def predict_diagnosis() -> DiagnosisResult:
    # هذا مثال وهمي (dummy) ـ غيّره بموديل فعلي عند دمج الذكاء الاصطناعي
    diseases = [
        "Pneumonia", "Tuberculosis", "COVID-19", "Normal", "Bronchitis"
    ]
    diagnosis = [
        DiseaseConfidence(disease=d, confidence=round(random.uniform(0, 1), 2))
        for d in diseases
    ]
    diagnosis_sorted = sorted(diagnosis, key=lambda x: x.confidence, reverse=True)
    return DiagnosisResult(diagnosis=diagnosis_sorted)

# يمكنك لاحقاً ربط هذه الدالة مع خدمة الذكاء الاصطناعي الفعلية مثل predictor.py أو rag_engine.py