from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.staffs.schemas import CreateStaff,UpdateStaff
from routers.users.account.models import User
from routers.staffs.models import Staff
from services.email import sendEmailToNewStaff


async def create_new_satff(staff:CreateStaff, db:Session):
    new_staff = Staff()
    new_staff.first_name = staff.first_name
    new_staff.last_name = staff.last_name
    new_staff.other_name = staff.other_name
    new_staff.gender = staff.gender
    new_staff.supervisor_id = staff.supervisor_id
    new_staff.department = staff.department
    new_staff.grade = staff.grade
    
    db.add(new_staff)
    db.flush()
    data = db.query(User).filter(User.staff_id == Staff.staff_id).first()
    db.refresh(new_staff, attribute_names=['staff_id'])
    #await sendEmailToNewStaff([data.email], new_staff)
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

