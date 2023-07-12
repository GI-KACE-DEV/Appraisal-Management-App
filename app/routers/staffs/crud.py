from multiprocessing import synchronize
from core.hashing import Hasher
from fastapi import status, Form, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from routers.staffs.schemas import CreateStaff, UpdateStaff
from routers.users.account.models import User
from routers.staffs.models import Staff 
from routers.appraisal_form.models import AppraisalForm, Appraisalview
from  dependencies import get_db
from services.email import sendEmailToNewStaff
#from passlib.context import CryptContext


async def create_new_staff_user(staff:CreateStaff, db: Session):
    #staff_object = Staff(**staff.dict())

    db_query = db.query(User).filter(User.email == staff.email).first()

    if db_query is not None:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
           detail="Staff with email (" + \
        str(staff.email) + ") already exists")
    

    staff_object = Staff(first_name = staff.first_name,last_name = staff.last_name,other_name = staff.other_name, appointment_date = staff.appointment_date,
    gender = staff.gender,supervisor_id = staff.supervisor_id,department = staff.department,grade = staff.grade, positions = staff.positions)
    db.add(staff_object)
    db.flush()

    user_object = User(email=staff.email, staff_id=staff_object.id, user_type_id= staff.user_type_id,reset_password_token=Hasher.generate_reset_password_token(), 
                       hashed_password=Hasher.get_password_hash(),is_active=True, is_superuser=False)
    
    db.add(user_object)
    db.flush()
    
    appraisalForm_object = AppraisalForm(department = staff.department,grade = staff.grade, positions = staff.positions,
    staff_id=staff_object.id)
    
    db.add(appraisalForm_object)
    db.flush()

    appraisal_view_object = Appraisalview(id=staff_object.id,first_name = staff.first_name,last_name = staff.last_name,email = staff.email,
    gender = staff.gender,supervisor_id = staff.supervisor_id,department = staff.department,grade = staff.grade, positions = staff.positions,
    appraisal_form_id=appraisalForm_object.id, reset_password_token=Hasher.generate_reset_password_token())


    db.add(appraisal_view_object)
    db.commit()
    db.refresh(staff_object)
    db.refresh(user_object)
    db.refresh(appraisal_view_object)
    #await sendEmailToNewStaff([staff.email], appraisal_view_object)
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








async def get_Admin_By_Token(token: str, db:Session):
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














async def get_Staff_By_email(email: str, db:Session):

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

