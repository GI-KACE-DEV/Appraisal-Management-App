from multiprocessing import synchronize
from sqlalchemy.orm import Session
from . import models, schemas
from core.config import settings




# def create_new_user(user:schemas.CreateUser, db:Session):
#     user = models.User(username=user.username, 
#                 email=user.email,
#                 hashed_password=(user.password),
#                 is_active=True,
#                 is_superuser=False
#                 )
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

## function for retrieving a job
def retreive_user(id:int, db:Session):
    item = db.query(models.User).filter(models.User.user_id == id).first() 
    return item 

## function for listing all jobs
def list_user(db: Session):
    jobs = db.query(models.User).all().filter(models.User.is_active == True)
    return jobs


## 
def update_user_by_id(id:int, user: schemas.CreateUser, db: Session, owner_id):
    existing_user = db.query(models.User).filter(models.User.user_id == id) 
    if not existing_user:
        return 0
    models.User.__dict__.update(owner_id==owner_id)
    existing_user.update(user.__dict__)
    db.commit()
    return 1


def delete_job_by_id(id:int, user:schemas.CreateUser, db: Session, owner_id):
    existing_user = db.query(models.User).filter(models.User.user_id == id)
    if not existing_user:
        return 0 
    existing_user.delete(synchronize_session=False)
    db.commit
    return 1