from multiprocessing import synchronize
from core.hashing import Hasher
from fastapi import status, Form, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from routers.staffs.schemas import CreateStaff
from routers.users.account.models import User
from routers.staffs.models import Staff 
from  dependencies import get_db
#from services.email import sendEmailToNewStaff
#from passlib.context import CryptContext


def create_new_staff_user(staff:CreateStaff, db: Session, staff_id: int):
    staff_object = Staff(**staff.dict())


    user_object = User(email=staff.email, hashed_password=Hasher.get_password_hash(),
                     is_active=True, is_superuser=False, 
                     created_at=staff.created_at, updated_at=staff.updated_at,)

    db.add(staff_object)
    db.add(user_object)
    db.commit()
    db.refresh(staff_object)
    db.refresh(user_object)
    return staff_object


# async def create_new_satff(db:Session, first_name:str = Form(...), last_name:str = Form(...),
#                 other_name:str = Form(None), email:str = Form(...),
#                 gender:str = Form(None) ,department:str = Form(None),
#                 grade:str = Form(None), supervisor_id:str = Form(None)):
    
#     new_staff = Staff()
#     new_staff.first_name = first_name
#     new_staff.last_name = last_name
#     new_staff.other_name = other_name
#     new_staff.gender = gender
#     new_staff.supervisor_id = supervisor_id
#     new_staff.department = department
#     new_staff.grade = grade

#     new_user = User()
#     new_user.email = email
#     new_user.hashed_password = pwd_context.hash("password")
#     new_user.staff_id = new_staff.staff_id
#     new_user.is_active = False

#     db.add(new_staff)
#     db.add(new_user)
#     db.flush()
#     data = db.query(User).filter(User.staff_id == Staff.staff_id).first()
#     db.refresh(new_staff, attribute_names=['staff_id'])
#     #await sendEmailToNewStaff([email], new_user)
#     db.commit()
#     db.close()
#     return new_staff


## function to get query all staff base on their active status
async def get_all_staff(db:Session):
    data = db.query(Staff).filter(Staff.is_active == True).all()
    return data


## function to get staff base on the staff id. 
async def getStaffById(id:int, db:Session):
    data = db.query(Staff).filter(Staff.staff_id == id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Staff with the id {id} is not found")
    return data







# async def updateStaff(updateStaff: UpdateStaff, db:Session):
#     staffID = updateStaff.staff_id
#     is_staffID_update = db.query(Staff).filter(Staff.staff_id == staffID).update({
#         Staff.first_name : updateStaff.first_name,
#         Staff.last_name : updateStaff.last_name,
#         Staff.other_name : updateStaff.other_name,
#         Staff.gender : updateStaff.gender,
#         Staff.supervisor_id : updateStaff.supervisor_id,
#         Staff.department : updateStaff.department,
#         Staff.grade : updateStaff.grade
#         }, synchronize_session=False)
#     db.flush()
#     db.commit()
#     if not is_staffID_update:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Staff with the id (" + str(staffID) + ") is not found")

#     data = db.query(Staff).filter(Staff.id == staffID).one()
#     return data


# async def deleteStaff(id: int, db:Session, staff_id):
#     # db_data = db.query(User).filter(User.user_id == staff_id).update({
#     #         User.is_active: False
#     #         }, synchronize_session=False)
#     # db.flush()
#     # db.commit()
#     # if not db_data:
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#     #         detail=f"Staff with the id {staff_id} is not found")

#     # data = db.query(Staff).filter(Staff.staff_id == id).first()
#     # if not data:
#     #     return 0
#     # db.delete()
#     # db.commit()

#     # existing_user = db.query(Staff).filter(Staff.staff_id == id)

#     # if not existing_user:
#     #     return 0
#     # existing_user.delete(synchronize_session=False)
#     # db.commit()

#     # return 1
    
#     # return 1

