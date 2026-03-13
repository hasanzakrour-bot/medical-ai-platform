from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, Patient, Diagnosis, DiagnosisResult
from schemas.user_schema import UserResponse
from api_server.utils.security import JWT_SECRET, JWT_ALGORITHM
from jose import jwt
from typing import List

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

# تحقق من صلاحية الادمن
def admin_required(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if payload.get("role") != "admin":
            raise HTTPException(status_code=403, detail="Admin only")
        return payload
    except:
        raise HTTPException(status_code=403, detail="Invalid token")


@router.get("/users", response_model=List[UserResponse])
def list_users(token: str, db: Session = Depends(get_db)):
    admin_required(token)
    users = db.query(User).all()
    return users


@router.post("/patients")
def add_patient(name: str, age: int, token: str, db: Session = Depends(get_db)):
    admin_required(token)
    patient = Patient(name=name, age=age)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return {"id": patient.id, "name": patient.name, "age": patient.age}


@router.get("/diagnosis")
def get_all_diagnosis(token: str, db: Session = Depends(get_db)):
    admin_required(token)
    diagnoses = db.query(Diagnosis).all()
    result = []
    for diag in diagnoses:
        items = [
            {"disease": r.disease, "confidence": r.confidence} for r in diag.results
        ]
        result.append({"diagnosis_id": diag.id, "patient_id": diag.patient_id, "results": items})
    return result