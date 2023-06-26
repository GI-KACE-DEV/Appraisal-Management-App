from  fastapi import  Depends
from exceptions import BlacklistedToken
from sqlalchemy.orm import Session
from dependencies import get_db
from . import models, schemas

def create_new_user(usertype:schemas.CreateUserType, db:Session = Depends(get_db)):
    usertype = models.User(title=usertype.title
                )
    db.add(usertype)
    db.commit()
    db.refresh(usertype)
    return usertype