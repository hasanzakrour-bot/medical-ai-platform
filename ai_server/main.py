from fastapi import FastAPI
from routers.ai_router import router as ai_router

app = FastAPI(
    title="Medical AI Server",
    version="1.0"
)

app.include_router(ai_router)