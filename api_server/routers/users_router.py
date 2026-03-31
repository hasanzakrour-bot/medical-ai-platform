from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def list_users():
    # استبدل بهذا استعلام فعلي من قاعدة بياناتك أو ORM
    return [{"username": "admin"}, {"username": "user1"}]

@router.get("/{user_id}")
def get_user(user_id: int):
    # استبدل بهذا استعلام فعلي من قاعدة بياناتك أو ORM
    return {"user_id": user_id, "username": f"user{user_id}"}