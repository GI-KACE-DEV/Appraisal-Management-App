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


@usertype_router.post("/id/{id}")
def get_user_type_by_id(id: str, db: Session = Depends(get_db)):
    
     data = crud.get_user_type_by_id(id, db=db)
     return data


@usertype_router.get("/all")
def read_usertypes(db: Session = Depends(get_db)):
    usertypes = list_usertypes(db=db)
    return usertypes
