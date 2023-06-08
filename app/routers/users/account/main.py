from fastapi import APIRouter, Depends
from dependencies import get_db
from sqlalchemy.orm import Session
from config import settings
from . import crud, schemas
from  dependencies import *

user_acc_router = APIRouter()

@user_acc_router.post("/create")
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    user = crud.create_new_user(user=user, db=db)
    return user 
