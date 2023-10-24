from core.hashing import Hasher
from routers.users.account.models import User, Administrator
from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session 
from . import models, schemas

from database import SessionLocal
from core.utils import raise_exc
from typing import Union


from jose import JWTError, jwt
from core.config import settings

def get_user(username: str,db: Session):
    
    user = db.query(models.User).filter_by(email=username).first()

    return user
        
def read_by_id(id:str, account:schemas.Account, db:Session):
    model = User if account=="users" else Administrator
    return db.query(model).get(id)

def read_by_email(email:str, account:str, db:Session):
    model = User if account=="users" else Administrator
    return db.query(model).filter_by(email=email).first()

def is_token_blacklisted(token:str, db:Session):
    return db.query(models.TokenTable.id).filter_by(access_toke=token).first() is not None

def add_email_verification_code(email, account:schemas.Account, db:Session):
    model = User if account=="users" else Administrator
    user = db.query(model).filter_by(email=email)
    if not user:
        raise HTTPException(status_code=404, detail=raise_exc("email", "user not found", "NotFound"))
    obj = models.EmailVerificationCode(email=email)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# async def revoke_token(payload:Union[schemas.Logout, str], db:Session):
#     try:
#         if isinstance(payload, str):
#             db.add(models.RevokedToken(jti=payload))
#         else:
#             db.add_all([models.RevokedToken(jti=token) for token in payload.dict().values()])
#         db.commit()
#         return 'success', 'token(s) successfully blacklisted'
#     except Exception as e: 
#         print(e)

async def log_revoke_token(token: str, db: Session):

    payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    #print(payload)
    id = payload['user_id']
    token_record = db.query(models.TokenTable).all()
    info=[]
    for record in token_record :
        print("record",record)
        if (datetime.utcnow() - record.created_date).days > 1:
            info.append(record.id)

    if info:
        existing_token = db.query(models.TokenTable).where(models.TokenTable.id.in_(info)).delete()
        db.commit()
        
    existing_token = db.query(models.TokenTable).filter(models.TokenTable.id == id, models.TokenTable.access_toke==token).first()
    if existing_token:
        existing_token.status=False
        db.add(existing_token)
        db.commit()
        db.refresh(existing_token)


    return {"message": "Logout Successfully"}

def del_code(email, db:Session=SessionLocal()):
    obj = db.query(models.EmailVerificationCode).get(email)
    if obj:
        db.delete(obj)
        db.commit()
    return True

def schedule_del_code(email):
    from core.config import settings
    return scheduler.add_job(
        del_code,
        trigger='date',
        kwargs={'email':email},
        id=f'ID-{email}',
        replace_existing=True,
        run_date=datetime.utcnow() + timedelta(minutes=settings.EMAIL_CODE_DURATION_IN_MINUTES)
    )
    