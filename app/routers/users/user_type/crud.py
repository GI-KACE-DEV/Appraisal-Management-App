from  fastapi import  Depends
from exceptions import BlacklistedToken
from sqlalchemy.orm import Session
from dependencies import get_db
from . import models, schemas
#from app.routers.users import user_type
#from app.routers.users import user_type

<<<<<<< HEAD
def create_new_user(payload:schemas.CreateUserType, db:Session = Depends(get_db)):
    ## lets check if an exiting user_type exist:
    
    usertype = models.UserType(title=payload.title)
    db.add(usertype)
    db.commit()
    db.refresh(usertype)
    return usertype 

def create_default_user_type():
    db: Session 
    ## lets query the db to see if we already have the default users before adding them
    usertypes = db.query(models.UserType).all()
    if not usertypes:
        
        admin = models.UserType(title="Admin")
        supervisor = models.UserType(title="Supervisor")
        user = models.UserType(title="User")
        
        db.add(admin)
        db.add(supervisor)
        db.add(user)
        db.commit()
        db.refresh(admin)
        db.refresh(supervisor)
        db.refresh(user)
        return admin, supervisor, user
    else:
        print('Admin, Supervisor, User already exist.')


def list_usertypes(db: Session):
    usertypes = db.query(models.UserType).all()
    if not usertypes:
        print('Hello')
    else:
        print('hi')
    return usertypes
   
=======
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
>>>>>>> a362d94599a120834c6ffb26344a2d795e75146b
