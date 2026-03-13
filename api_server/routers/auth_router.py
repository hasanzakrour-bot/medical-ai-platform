from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.user_schema import UserCreate, UserLogin
from services.auth_service import create_user, login_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/register")

def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    created = create_user(
        db,
        user.email,
        user.password,
        user.role
    )

    return {
        "id": created.id,
        "email": created.email,
        "role": created.role
    }


@router.post("/login")

def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        user.email,
        user.password
    )

    if not token:

        return {"error": "invalid credentials"}

    return {"access_token": token}