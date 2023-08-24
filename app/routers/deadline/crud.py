from multiprocessing import synchronize
from core.hashing import Hasher
from fastapi import status, Form, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from routers.deadline.schemas import CreateDeadline, UpdateDeadline
from routers.deadline.models import DepartmentDeadline, StaffDeadline
from routers.users.user_type.models import UserType
from routers.staffs.models import Staff 
from routers.appraisal_form.models import AppraisalForm
from  dependencies import get_db
from routers.staffs.models import Staff 
from datetime import datetime
from routers.users.account.models import User




# function for creating deadline
async def create_deadline(deadline:CreateDeadline, db: Session):
    year = datetime.now()
    current_year = year.year

    # check if user creating deadline is supervisor
    db_user_type = db.query(Staff).filter(
        User.staff_id == Staff.id,
        UserType.id == User.user_type_id,
        UserType.title == "Supervisor",
        Staff.id == deadline.supervisor_id
        ).first()

    if not db_user_type:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
                            detail="Deadline is created by only Supervisors")
    
    # creating of Departmental Deadline by only supervisor
    deadline_object = DepartmentDeadline(**deadline.dict())
    deadline_object.deadline_year = current_year
    db.add(deadline_object)
    db.flush()
    
    #extracting staff info to create appraisal_form for all staff if only deadline is start of year(only staff under the supervisor)
    db_data = db.query(Staff).filter(Staff.supervisor_id == deadline.supervisor_id).all()

    #creating appraisal_form for staff if deadline is start of year
    if deadline.deadline_type == "Start" or deadline.deadline_type == "First":
        for row in db_data:
            appraisalForm_object = AppraisalForm(department= row.department, grade=row.grade,appraisal_year= current_year,
                                                supervisor_id=row.supervisor_id,positions=row.positions, staff_id=row.id)
            db.add(appraisalForm_object)
            db.flush()
            db.refresh(appraisalForm_object)

            # creating individual start of year deadline for all staff
            start_staff_deadline = StaffDeadline(**deadline.dict())
            start_staff_deadline.deadline_year = current_year
            start_staff_deadline.appraisal_form_id = appraisalForm_object.id
            db.add(start_staff_deadline)
            db.flush()
            db.commit()
            db.refresh(start_staff_deadline)

            # creating appraisal_form_id for all staff after deadline been created for start of year
            db.query(Staff).filter(Staff.id == row.id, Staff.supervisor_id == deadline.supervisor_id).update({
            Staff.appraisal_form_id : appraisalForm_object.id,
            }, synchronize_session=False)
            db.flush()
    
    #extracting appraisal_form_id to create mid year deadline for all staff
    mid_AppraisalForm = db.query(AppraisalForm).filter(
        AppraisalForm.appraisal_year == current_year, 
        AppraisalForm.supervisor_id == deadline.supervisor_id).all()

    # creating individual mid year deadline for all staff
    if deadline.deadline_type == "Mid" or deadline.deadline_type == "Second":
        for row in mid_AppraisalForm:
            mid_staff_deadline = StaffDeadline(**deadline.dict())
            mid_staff_deadline.deadline_year = current_year
            mid_staff_deadline.appraisal_form_id = row.id
            db.add(mid_staff_deadline)
            db.flush()
            db.commit()
            db.refresh(mid_staff_deadline)

    #extracting appraisal_form_id to create end of year deadline for all staff
    end_AppraisalForm = db.query(AppraisalForm).filter(
        AppraisalForm.appraisal_year == current_year, 
        AppraisalForm.supervisor_id == deadline.supervisor_id).all()

    # creating individual end of year deadline for all staff
    if deadline.deadline_type == "End" or deadline.deadline_type == "Third":
        for row in end_AppraisalForm:
            mid_staff_deadline = StaffDeadline(**deadline.dict())
            mid_staff_deadline.deadline_year = current_year
            mid_staff_deadline.appraisal_form_id = row.id
            db.add(mid_staff_deadline)
            db.flush()
            db.commit()
            db.refresh(mid_staff_deadline)
    db.commit()
    db.refresh(deadline_object)
    return "(" + str(deadline_object.deadline_type) + ") deadline created successfuly"












async def get_deadline(db:Session):
    return db.query(DepartmentDeadline).all()









async def get_deadline_by_supervisor_id(supervisor_id: int, db:Session):
    year = datetime.now()
    current_year = year.strftime("%Y")
    data = db.query(DepartmentDeadline).filter(
        DepartmentDeadline.deadline_year == current_year,
        DepartmentDeadline.supervisor_id == supervisor_id).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department Deadline {supervisor_id} not found")

    return data











async def get_deadline_by_id(id: int, db:Session):
    year = datetime.now()
    current_year = year.strftime("%Y")
    data = db.query(DepartmentDeadline).filter(
        DepartmentDeadline.deadline_year == current_year,
        DepartmentDeadline.id == id).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Department Deadline {id} not found")

    return data









async def update_department_deadline(updateDeadline: UpdateDeadline, db:Session):
    deadline_id = updateDeadline.id
    is_mid_year_review_id_update = db.query(DepartmentDeadline).filter(DepartmentDeadline.id == deadline_id).update({
        DepartmentDeadline.deadline_type : updateDeadline.deadline_type,
        DepartmentDeadline.deadline_year : updateDeadline.deadline_year,
        DepartmentDeadline.start_date : updateDeadline.start_date,
        DepartmentDeadline.end_date : updateDeadline.end_date,
        DepartmentDeadline.comment : updateDeadline.comment
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_mid_year_review_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Deadline with the id (" + str(deadline_id) + ") is not found")

    data = db.query(DepartmentDeadline).filter(DepartmentDeadline.id == deadline_id).first()

    update_staff_deadline = db.query(DepartmentDeadline).filter(
        StaffDeadline.deadline_year == data.deadline_year,
        StaffDeadline.supervisor_id == data.supervisor_id,
        StaffDeadline.deadline_type == data.deadline_type
        ).first()
    
    if update_staff_deadline:
        db.query(StaffDeadline).filter(
                StaffDeadline.deadline_year == data.deadline_year,
                StaffDeadline.supervisor_id == data.supervisor_id,
                StaffDeadline.deadline_type == data.deadline_type
                ).update({
                StaffDeadline.start_date : updateDeadline.start_date,
                StaffDeadline.end_date : updateDeadline.end_date
            }, synchronize_session=False)
        db.flush()
        db.commit()

    return "Deadline updated successfully"