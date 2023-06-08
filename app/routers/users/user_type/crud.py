from utils import raise_exc, decode_jwt, schema_to_model, create_jwt
from ..auth.crud import is_token_blacklisted, revoke_token
from ..auth.models import EmailVerificationCode
from  fastapi import HTTPException, Depends
from exceptions import BlacklistedToken
from sqlalchemy.orm import Session
from ..auth.schemas import Logout
from dependencies import get_db
from . import models, schemas
from config import settings
from cls import CRUD

def create_new_user(usertype:schemas.CreateUserType, db:Session = Depends(get_db)):
    usertype = models.User(title=usertype.title
                )
    db.add(usertype)
    db.commit()
    db.refresh(usertype)
    return usertype