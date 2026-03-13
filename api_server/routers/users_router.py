from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Patient, Diagnosis, DiagnosisResult
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/patients/{patient_id}/diagnosis")
def get_patient_diagnosis(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    diagnoses = db.query(Diagnosis).filter(Diagnosis.patient_id == patient_id).all()
    result = []
    for diag in diagnoses:
        items = [{"disease": r.disease, "confidence": r.confidence} for r in diag.results]
        result.append({"diagnosis_id": diag.id, "results": items})
    return result