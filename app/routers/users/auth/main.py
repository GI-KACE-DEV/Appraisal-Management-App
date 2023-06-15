from fastapi import Depends,APIRouter, status,HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt

from pydantic import EmailStr 

from dependencies import get_db
from core.hashing import Hasher
from .schemas import Token

from .crud import get_user
from core.security import create_access_token
from core.config import settings


auth_router = APIRouter()

def authenticate_user(email: str, password: str,db: Session):
    user = get_user(email=email,db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


@auth_router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session= Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    print(user)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

##
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")
## lets create a function to identify a current user
def get_current_user_from_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials", 
    )

    try:
        payload = jwt.decode(token, settings.SECRETE_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        print("username/email extracted is", username)
        if username is None:
            raise credentials_exception
    except JwTError:
        raise credentials_exception
    user = get_user(username=username, db=db)
    if user is None:
        raise credentials_exception 
    return user 
