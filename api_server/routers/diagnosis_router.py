from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from ai_server.models.predictor import predict_xray

router = APIRouter(
    prefix="/diagnosis",
    tags=["Diagnosis"]
)

@router.post("/xray")
async def diagnose_xray(file: UploadFile = File(...)):
    result = predict_xray(file)
    return JSONResponse(content=result)

# يمكنك إضافة نقاط تشخيص لتحاليل أو أدوات طبية أخرى مستقبلاً