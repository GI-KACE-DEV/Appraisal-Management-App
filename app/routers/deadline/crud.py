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




async def create_deadline(deadline:CreateDeadline, db: Session):
    year = datetime.now()
    appraisal_year = year.year

    db_user_type = db.query(Staff).filter(
        User.staff_id == Staff.id,
        UserType.id == User.user_type_id,
        UserType.title == "Supervisor",
        Staff.id == deadline.supervisor_id
        ).first()

    if not db_user_type:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
                            detail="Deadline is created by only Supervisors")
    
    deadline_object = DepartmentDeadline(**deadline.dict())
    deadline_object.deadline_year = appraisal_year
    db.add(deadline_object)
    db.flush()
    
    db_data = db.query(Staff).filter(Staff.supervisor_id == deadline.supervisor_id).all()

    if deadline.deadline_type == "Start" or deadline.deadline_type == "First":
        for row in db_data:
            appraisalForm_object = AppraisalForm(department= row.department, grade=row.grade,appraisal_year= appraisal_year,
                                                supervisor_id=row.supervisor_id,positions=row.positions, staff_id=row.id)
            db.add(appraisalForm_object)
            db.flush()
            db.refresh(appraisalForm_object)

            staffDeadline_object = StaffDeadline(**deadline.dict())
            staffDeadline_object.deadline_year = appraisal_year
            staffDeadline_object.appraisal_form_id = appraisalForm_object.id
            db.add(staffDeadline_object)
            db.flush()
            db.commit()
            db.refresh(staffDeadline_object)

            db.query(Staff).filter(Staff.id == row.id, Staff.supervisor_id == deadline.supervisor_id).update({
            Staff.appraisal_form_id : appraisalForm_object.id,
            }, synchronize_session=False)
            db.flush()
        
    db.commit()
    db.refresh(deadline_object)
    return "(" + str(deadline_object.deadline_type) + ") deadline created successfuly"











async def update_department_deadline(updateDeadline: UpdateDeadline, db:Session):
    deadline_id = updateDeadline.id
    is_mid_year_review_id_update = db.query(DepartmentDeadline).filter(DepartmentDeadline.id == deadline_id).update({
        DepartmentDeadline.deadline_type : updateDeadline.deadline_type,
        DepartmentDeadline.start_date : updateDeadline.start_date,
        DepartmentDeadline.end_date : updateDeadline.end_date
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_mid_year_review_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Deadline with the id (" + str(deadline_id) + ") is not found")

    data = db.query(DepartmentDeadline).filter(DepartmentDeadline.id == deadline_id).one()
    return data