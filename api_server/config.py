import os

DB_URL = os.environ.get("DB_URL", "sqlite:///./test.db")
DEBUG = bool(os.environ.get("DEBUG", True))
SECRET_KEY = os.environ.get("SECRET_KEY", "supersecret")
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*").split(",")