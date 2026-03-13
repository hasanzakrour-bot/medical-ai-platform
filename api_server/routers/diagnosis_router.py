from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
import requests
from schemas.diagnosis_schema import DiagnosisCreate
from services.diagnosis_service import save_diagnosis

router = APIRouter(
    prefix="/diagnosis",
    tags=["Diagnosis"]
)

AI_SERVER_URL = "http://ai_server:8001/ai/diagnose/xray"

@router.post("/upload")
async def upload_xray(patient_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):

    # إرسال الصورة إلى AI Server
    files = {"file": (file.filename, await file.read(), file.content_type)}
    response = requests.post(AI_SERVER_URL, files=files)
    result = response.json()

    # بناء schema للتخزين
    diag_schema = DiagnosisCreate(
        patient_id=patient_id,
        results=result["diagnosis"]
    )

    diag = save_diagnosis(db, diag_schema)

    return {"message": "Diagnosis saved successfully", "diagnosis_id": diag.id}