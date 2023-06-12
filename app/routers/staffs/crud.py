from fastapi.exceptions import HTTPException
from fastapi import status, Form
from sqlalchemy.orm import Session
from routers.staffs.schemas import CreateStaff,UpdateStaff
from routers.users.account.models import User
from routers.staffs.models import Staff
from services.email import sendEmailToNewStaff
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_new_satff(db:Session, first_name:str = Form(...), last_name:str = Form(...),
                other_name:str = Form(None), email:str = Form(...),
                gender:str = Form(None) ,department:str = Form(None),
                grade:str = Form(None), supervisor_id:str = Form(None)):
    
    new_staff = Staff()
    new_staff.first_name = first_name
    new_staff.last_name = last_name
    new_staff.other_name = other_name
    new_staff.gender = gender
    new_staff.supervisor_id = supervisor_id
    new_staff.department = department
    new_staff.grade = grade

    new_user = User()
    new_user.email = email
    new_user.hashed_password = pwd_context.hash("password")
    new_user.staff_id = new_staff.staff_id
    new_user.is_active = False

    db.add(new_staff)
    db.add(new_user)
    db.flush()
    data = db.query(User).filter(User.staff_id == Staff.staff_id).first()
    db.refresh(new_staff, attribute_names=['staff_id'])
    #await sendEmailToNewStaff([email], new_user)
    db.commit()
    db.close()
    return new_staff





async def get_all_staff(db:Session):
    data = db.query(Staff).filter(Staff.staff_id == User.staff_id).filter(User.is_active == True).all()
    return data






async def getStaffById(id: int, db:Session):
    data = db.query(Staff).filter(Staff.staff_id == id).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Staff with the id {id} is not found")
    return data







async def updateStaff(updateStaff: UpdateStaff, db:Session):
    staffID = updateStaff.staff_id
    is_staffID_update = db.query(Staff).filter(Staff.staff_id == staffID).update({
        Staff.first_name : updateStaff.first_name,
        Staff.last_name : updateStaff.last_name,
        Staff.other_name : updateStaff.other_name,
        Staff.gender : updateStaff.gender,
        Staff.supervisor_id : updateStaff.supervisor_id,
        Staff.department : updateStaff.department,
        Staff.grade : updateStaff.grade
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_staffID_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Staff with the id (" + str(staffID) + ") is not found")

    data = db.query(Staff).filter(Staff.id == staffID).one()
    return data










async def deleteStaff(id: int, db:Session):
    db_data = db.query(User).filter(User.staff_id == id).update({
            User.is_active: False
            }, synchronize_session=False)
    db.flush()
    db.commit()
    if not db_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Staff with the id {id} is not found")

    data = db.query(Staff).filter(Staff.staff_id == id).one()
    return data

