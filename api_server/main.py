from fastapi import FastAPI
from routers import auth_router, users_router, admin_router, diagnosis_router

app = FastAPI(
    title="Medical AI API",
    version="1.0"
)

app.include_router(auth_router.router)
app.include_router(users_router.router)
app.include_router(admin_router.router)
app.include_router(diagnosis_router.router)