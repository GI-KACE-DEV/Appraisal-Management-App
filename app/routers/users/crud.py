from sqlalchemy.orm import Session

from app.routers.users.schemas import CreateUser
from app.routers.users.models import User
from core.hashing import Hasher


def create_new_user(user:CreateUser, db:Session):
    user = User(username=user.username, 
                email=user.email,
                hashed_password=Hasher.get_password_hash(user.password),
                is_active=True,
                is_superuser=False
                )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user