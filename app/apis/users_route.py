from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.routers.users.schemas import CreateUser, ShowUser
from app.db.session import get_db
from app.routers.users.crud import create_new_user


router = APIRouter()


@router.post("/", response_model = ShowUser)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user 

