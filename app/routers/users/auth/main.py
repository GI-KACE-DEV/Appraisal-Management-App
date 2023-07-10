from . import schemas, crud
from fastapi import Depends,APIRouter, status,HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt

from pydantic import EmailStr 

from dependencies import get_db
from core.hashing import Hasher
from .schemas import Token

from .crud import authenticate_user
from core.security import create_access_token
from core.config import settings
from core.utils import create_jwt

auth_router = APIRouter()


@auth_router.post('/login', response_model=schemas.LoginResponse, name='Login')
async def login_for_access_token(payload:schemas.Login, db:Session=Depends(get_db)):
    user = await authenticate_user(payload, db)

    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="account is not active")

    # if not user.is:
    #     raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="account is not a super user")

    data = {"sub":user.email}
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data=data,
        expires_delta=access_token_expires
    )
    refresh_token = create_access_token(
        data=data,
        expires_delta=access_token_expires
    )
    return {
        "access_token": access_token, 
        "refresh_token": refresh_token,
        "user":user,
        
    }

@auth_router.post("/logout", name='Logout')
async def logout(payload:schemas.Logout, db:Session=Depends(get_db)):
    return await crud.revoke_token(payload, db)