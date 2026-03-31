from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

class UserLoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: UserLoginRequest):
    # استبدل بهذا منطق التحقق فعلياً
    if user.username == "admin" and user.password == "admin":
        return {"access_token": "dummy-token", "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

# أضف نقاط التسجيل، تجديد الجلسة، الخروج... حسب الحاجة