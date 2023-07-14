from  fastapi import  Depends
from exceptions import BlacklistedToken
from sqlalchemy.orm import Session
from dependencies import get_db
from . import models, schemas

def create_new_user(usertype:schemas.CreateUserType, db:Session = Depends(get_db)):
    usertype = models.UserType(title=usertype.title
                )
    db.add(usertype)
    db.commit()
    db.refresh(usertype)
    return usertype







async def get_all_user_type(db:Session):
    data = db.query(models.UserType).all()
    return data
