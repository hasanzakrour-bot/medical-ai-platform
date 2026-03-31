from fastapi import APIRouter, Depends, HTTPException, status
from api_server.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

# مثال: نقطة وصول لجلب جميع المستخدمين (تتطلب صلاحية أدمن)
@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    # هنا من الأفضل أن تربط بجدول المستخدمين باستخدام ORM
    # users = db.query(User).all()
    # return users
    return {"message": "هذه نقطة وصول خاصة بالأدمن لجلب المستخدمين (يرجى ربط قاعدة البيانات فعلياً)"}

# يمكنك إضافة المزيد من النقاط مثل (إحصائيات، تحكم بالنظام...) حسب الحاجة