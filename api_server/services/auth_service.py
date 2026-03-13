from sqlalchemy.orm import Session
from api_server.utils.security import hash_password, verify_password
from api_server.utils.security import create_access_token
from models import User


def create_user(db: Session, email: str, password: str, role: str):

    hashed = hash_password(password)

    user = User(
        email=email,
        password=hashed,
        role=role
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:

        return None

    if not verify_password(password, user.password):

        return None

    token = create_access_token(
        {
            "user_id": user.id,
            "role": user.role
        }
    )

    return token