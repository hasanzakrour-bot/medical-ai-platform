from pydantic import BaseModel
from typing import List, Optional

class DiseaseConfidence(BaseModel):
    disease: str
    confidence: float

class DiagnosisResult(BaseModel):
    diagnosis: List[DiseaseConfidence]

class XRayRequest(BaseModel):
    # إذا كنت تحتاج بيانات إضافية في الطلب كالـ patient_id أو أي وسوم أخرى أضفها هنا
    pass

class RAGRequest(BaseModel):
    question: str

class RAGResponse(BaseModel):
    answer: str