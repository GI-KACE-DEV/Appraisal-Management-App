from urllib import response
from fastapi import APIRouter, Depends, HTTPException, Request
from dependencies import get_db

from typing import Union, List, Optional

from sqlalchemy.orm import Session
from . import crud, schemas
from .schemas import CreateUserType, ShowUserType
from .crud import create_new_user, create_default_user_type, list_usertypes
import re
from  dependencies import *

usertype_router = APIRouter()


@usertype_router.post("/")
def create_usertype(payload: CreateUserType, db: Session = Depends(get_db)):
    usertype = crud.create_new_user(payload=payload, db=db)
    return usertype 

#@usertype_router.post("/create-usertype")
def create_default_user_types():
    db: Session 
    df_usertype = crud.create_default_user_type(db=db)
    return df_usertype 

@usertype_router.get("/all", response_model=List[ShowUserType])
def read_usertypes(db: Session = Depends(get_db)):
    usertypes = list_usertypes(db=db)
    return usertypes
