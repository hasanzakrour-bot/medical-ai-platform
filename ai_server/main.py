from fastapi import FastAPI
from ai_server.routers.ai_router import router as ai_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Medical AI Server",
    version="1.0",
    description="API for the Medical AI Platform: Supports Chest X-ray Diagnosis and Medical RAG QA"
)

# تفعيل CORS (اجعله مفتوحاً أثناء التطوير)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # غيّر هذا في الإنتاج إلى الدومين المصرح فقط
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# دمج الراوتر الذكي
app.include_router(ai_router)