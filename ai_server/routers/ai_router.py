from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from models.predictor import predict_xray
from rag.rag_engine import rag_answer

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post("/diagnose/xray")
async def diagnose_xray(file: UploadFile = File(...)):
    result = predict_xray(file)
    return JSONResponse(content=result)

@router.post("/rag")
async def query_rag(question: str = Form(...)):
    answer = rag_answer(question)
    return JSONResponse(content={"answer": answer})