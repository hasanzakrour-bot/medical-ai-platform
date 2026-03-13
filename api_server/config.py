import os

JWT_SECRET = os.getenv("JWT_SECRET", "super_secret_key")

JWT_ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/medical_ai"
)

AI_SERVER_URL = os.getenv(
    "AI_SERVER_URL",
    "http://ai_server:8001"
)