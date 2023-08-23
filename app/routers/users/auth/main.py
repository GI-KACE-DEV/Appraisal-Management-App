from lib2to3.pgen2 import token
from routers.users.auth.models import TokenTable
from . import schemas, crud
from fastapi import Depends,APIRouter, status,HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated

from jose import JWTError, jwt

from pydantic import EmailStr 

from dependencies import get_db
from core.hashing import Hasher
from .schemas import TokenCreate
from .crud import  get_user
from core.security import create_access_token
from core.config import settings
from core.utils import create_jwt 


auth_router = APIRouter()

def authenticate_user(username: str, password: str, db: Session):

    user = get_user(username=username, db=db)
    
    if not user:
        return False
             
    if not Hasher.verify_password(password, user.hashed_password):
        return False 

    return user

@auth_router.post('/token', response_model=schemas.LoginResponse, name='Login')
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db:Session=Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="account is not active")

    # if not user.is:
    #     raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="account is not a super user")

    data = {"sub": user.email, "user_id": user.id}

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data=data,
        expires_delta=access_token_expires
    )

    refresh_token = create_access_token(
        data=data,
        expires_delta=access_token_expires
    )

    token_db = TokenTable(id=user.id, access_toke=access_token, refresh_toke=refresh_token, status=True)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    return {

        "access_token": access_token, 
        "refresh_token": refresh_token,
        "user":user,

    }


## 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 
    
    
## lets create a function to create a dependency to indentify a current user
def get_current_user_from_token(token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )

    try:

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        print("username/email extracted is ", username)
        
    except JWTError:
        raise credentials_exception
    
    user = get_user(username=username, db=db)

    if user is None:
        raise credentials_exception
    return user 

# @auth_router.post("/logout", name='Logout')
# async def logout(payload:schemas.Logout, db:Session=Depends(get_db)):
#     return await crud.revoke_token(payload, db)

@auth_router.post("/logout", name='Logout')
async def logout(token: str = Depends(oauth2_scheme), db:Session=Depends(get_db)):
    #print(token)
    return await crud.log_revoke_token(token, db)