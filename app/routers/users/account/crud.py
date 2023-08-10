from multiprocessing import synchronize
from sqlalchemy.orm import Session
from . import models, schemas
from core.config import settings
from routers.users.account.models import User
from fastapi import status
from fastapi.exceptions import HTTPException
from routers.appraisal_form.models import Appraisalview
from core.hashing import Hasher
from routers.staffs.schemas import UpdateStaff






## function for retrieving a job
def retreive_user(id:int, db:Session):
    item = db.query(models.User).filter(models.User.id == id).first() 
    return item 

## function for listing all jobs
def list_user(db: Session):
    jobs = db.query(models.User).all().filter(models.User.is_active == True)
    return jobs








## function to get staff base on the email.
async def get_user_by_email(email: str, db:Session):

    user_db_data = db.query(User).filter(User.email == email).update({
        User.hashed_password : None,
        User.reset_password_token : Hasher.generate_reset_password_token()
        }, synchronize_session=False)
    
    if not user_db_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff with email (" + str(email) + ") is not found")

    db.query(Appraisalview).filter(Appraisalview.email == email).update({
        Appraisalview.reset_password_token : Hasher.generate_reset_password_token()
        }, synchronize_session=False)
    db.flush()
    db.commit()
    data = db.query(Appraisalview).filter(Appraisalview.email == email).one()
    return data








## function to get staff base on the token.
async def get_user_By_Token(token: str, db:Session):
    db_data = db.query(User).filter(User.reset_password_token == token).update({
        User.hashed_password : None
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not db_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Token")
    data = db.query(Appraisalview).filter(Appraisalview.reset_password_token == token).one()
    return data













## function to update user after reset password.
async def update_Staff_After_Reset_Password(updateStaff: UpdateStaff, db:Session):
    staffID = updateStaff.id
    is_staffID_update = db.query(User).filter(User.staff_id == staffID).update({
        User.reset_password_token : None,
        User.hashed_password : Hasher.empty_password_hash(updateStaff.hashed_password)
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_staffID_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff with the id (" + str(staffID) + ") is not found")
    
    db.query(Appraisalview).filter(Appraisalview.id == staffID).update({
        Appraisalview.reset_password_token : None
        }, synchronize_session=False)
    db.flush()
    db.commit()
    data = db.query(Appraisalview).filter(Appraisalview.id == staffID).one()
    return data














## 
def update_user_by_id(id:int, user: schemas.CreateUser, db: Session, owner_id):
    existing_user = db.query(models.User).filter(models.User.id == id) 
    if not existing_user:
        return 0
    models.User.__dict__.update(owner_id==owner_id)
    existing_user.update(user.__dict__)
    db.commit()
    return 1


def delete_job_by_id(id:int, user:schemas.CreateUser, db: Session, owner_id):
    existing_user = db.query(models.User).filter(models.User.id == id)
    if not existing_user:
        return 0 
    existing_user.delete(synchronize_session=False)
    db.commit
    return 1