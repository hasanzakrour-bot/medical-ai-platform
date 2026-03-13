from sqlalchemy.orm import Session
from models import Diagnosis, DiagnosisResult
from schemas.diagnosis_schema import DiagnosisCreate

def save_diagnosis(db: Session, diagnosis: DiagnosisCreate):

    diag = Diagnosis(patient_id=diagnosis.patient_id)
    db.add(diag)
    db.commit()
    db.refresh(diag)

    # حفظ كل نتيجة
    for item in diagnosis.results:
        res = DiagnosisResult(
            diagnosis_id=diag.id,
            disease=item.disease,
            confidence=item.confidence
        )
        db.add(res)
    db.commit()
    return diag