from pydantic import BaseModel
from typing import List, Dict

class DiagnosisItem(BaseModel):
    disease: str
    confidence: float

class DiagnosisCreate(BaseModel):
    patient_id: int
    results: List[DiagnosisItem]

class DiagnosisResponse(BaseModel):
    id: int
    patient_id: int
    results: List[DiagnosisItem]