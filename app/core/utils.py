from jose import JWTError, jwt

from datetime import timedelta, datetime, date
from .config import * 

from fastapi import APIRouter, Depends, HTTPException, Request
from dependencies import get_db
from sqlalchemy.orm import Session

from routers.users.user_type.crud import create_default_user_type

def create_jwt(data:dict, exp:timedelta=None):
    data.update({'exp':datetime.utcnow() + timedelta(minutes=exp if exp else settings.ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_jwt(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)

def raise_exc(loc=None, msg=None, type=None):
    detail = {}
    if loc:
        detail.update({"loc":loc if loc.__class__ in [list, set, tuple] else [loc]})
    if msg:
        detail.update({"msg":msg})
    if msg:
        detail.update({"type":type})
    return [detail] 

async def create_default_users():
    df_usertype = create_default_user_type()
    return df_usertype