from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_server.routers import admin_router ,auth_router,diagnosis_router,users_router
from api_server.config import ALLOWED_ORIGINS

app = FastAPI(
    title="Medical AI Server",
    version="1.0",
    description="API for Medical AI Platform"
)

# تفعيل CORS بالاعتماد على الإعدادات
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin_router)
app.include_router(auth_router)
app.include_router(diagnosis_router)
app.include_router(users_router)