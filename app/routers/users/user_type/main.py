from fastapi import APIRouter, Depends, HTTPException, Request
from dependencies import get_db, validate_bearer
from utils import r_fields, urljoin, logger
from typing import Union, List, Optional
#from rds.tasks import async_send_email
#from cls import ContentQueryChecker
from sqlalchemy.orm import Session
from config import settings
from . import crud, schemas
import re
from  dependencies import *

usertype_router = APIRouter()


@usertype_router.post("/")
def create_usertype(usertype: schemas.CreateUserType, db: Session = Depends(get_db)):
    usertype = crud.create_new_user(usertype=usertype, db=db)
    return usertype