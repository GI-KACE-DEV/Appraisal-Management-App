from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends,APIRouter, status,HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta


from app.core.config import settings
from app.db.session import get_db
from app.core.hashing import Hasher
from app.core.jwt_tokens import create_access_token
from app.routers.users.schemas import Token 
from app.routers.users.models import User


router = APIRouter()



## lets create a function that would return a user given the email
def get_user(username: str, db: Session):
    user = db.query(User).filter(User.email == username).first()

    return user



def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username=username,db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
