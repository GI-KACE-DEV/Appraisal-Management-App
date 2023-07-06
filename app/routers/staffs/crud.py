from multiprocessing import synchronize
from core.hashing import Hasher
from fastapi import status, Form, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from routers.staffs.schemas import CreateStaff
from routers.users.account.models import User
from routers.staffs.models import Staff 
from routers.appraisal_form.models import AppraisalForm, Appraisalview
from  dependencies import get_db
#from services.email import sendEmailToNewStaff
#from passlib.context import CryptContext


def create_new_staff_user(staff:CreateStaff, db: Session):
    #staff_object = Staff(**staff.dict())

    db_query = db.query(User).filter(User.email == staff.email).first()

    if db_query is not None:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
           detail=f"Staff with email (" + \
        str(staff.email) + ") already exists")
    

    staff_object = Staff(first_name = staff.first_name,last_name = staff.last_name,other_name = staff.other_name,
    gender = staff.gender,supervisor_id = staff.supervisor_id,department = staff.department,grade = staff.grade, positions = staff.positions)
    db.add(staff_object)
    db.flush()

    user_object = User(email=staff.email, staff_id=staff_object.id,  hashed_password=Hasher.get_password_hash(),
                     is_active=True, is_superuser=False)
    
    db.add(user_object)
    db.flush()
    
    appraisalForm_object = AppraisalForm(department = staff.department,grade = staff.grade, positions = staff.positions,
    staff_id=staff_object.id)
    
    db.add(appraisalForm_object)
    db.flush()

    appraisal_view_object = Appraisalview(id=staff_object.id,first_name = staff.first_name,last_name = staff.last_name,email = staff.email,
    gender = staff.gender,supervisor_id = staff.supervisor_id,department = staff.department,grade = staff.grade,
    positions = staff.positions,appraisal_form_id=appraisalForm_object.id)


    db.add(appraisal_view_object)
    db.commit()
    db.refresh(staff_object)
    db.refresh(user_object)
    db.refresh(appraisal_view_object)
    return appraisal_view_object












## function to get query all staff base on their active status
async def get_all_staff(db:Session):
    data = db.query(Appraisalview).filter(Appraisalview.is_active == True).all()
    return data





## function to get staff base on the staff id. 
async def getStaffById(id:int, db:Session):

    data = db.query(Appraisalview).filter(Appraisalview.id == id).first()

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

