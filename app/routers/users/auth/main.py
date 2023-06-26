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

from .crud import verify_user
from core.security import create_access_token
from core.config import settings
from core.utils import create_jwt
2
auth_router = APIRouter()


@auth_router.post('/login', response_model=schemas.LoginResponse, name='Login')
async def authenticate(payload:schemas.Login, account:schemas.Account, db:Session=Depends(get_db)):
    user = await verify_user(payload, account.value, db)

    # if not user.is_active:
    #     raise HTTPException(status_code, detail="account is not active")

    # if not user.is_superuser:
    #     raise HTTPException(status_code, detail="account is not a super user")

    data = {"id":user.email, "account":account.value}

    return {
        "access_token":create_jwt(data=data, exp=settings.ACCESS_TOKEN_DURATION_IN_MINUTES),
        "refresh_token":create_jwt(data=data, exp=settings.REFRESH_TOKEN_DURATION_IN_MINUTES),
        "account":account.value,
        "user":user
    }

@auth_router.post("/logout", name='Logout')
async def logout(payload:schemas.Logout, db:Session=Depends(get_db)):
    return await crud.revoke_token(payload, db)