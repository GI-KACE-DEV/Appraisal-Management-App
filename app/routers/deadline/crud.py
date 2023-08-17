from multiprocessing import synchronize
from core.hashing import Hasher
from fastapi import status, Form, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from routers.deadline.schemas import CreateDeadline, UpdateDeadline
from routers.deadline.models import Deadline
from routers.users.user_type.models import UserType
from routers.staffs.models import Staff 
from routers.appraisal_form.models import AppraisalForm, Appraisalview
from  dependencies import get_db
from routers.staffs.models import Staff 
from datetime import datetime




async def create_deadline(deadline:CreateDeadline, db: Session):
    year = datetime.now()
    appraisal_year = year.year

    db_user_type = db.query(Staff).filter(
        UserType.id == Staff.user_type_id,
        UserType.title == "Supervisor",
        Staff.id == deadline.supervisor_id
        ).first()

    if not db_user_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Deadline is created by only Supervisors")
    
    deadline_object = Deadline(**deadline.dict())
    deadline_object.deadline_year = appraisal_year
    db.add(deadline_object)
    db.flush()
    
    db_data = db.query(Appraisalview).filter(Appraisalview.supervisor_id == deadline.supervisor_id).all()

    if deadline.deadline_type == "Start of Year" or deadline.deadline_type == "First Phase":
        for row in db_data:
            appraisalForm_object = AppraisalForm(department= row.department, grade=row.grade,appraisal_year= appraisal_year,
                                                supervisor_id=row.supervisor_id,positions=row.positions, staff_id=row.staff_id)
            db.add(appraisalForm_object)
            db.flush()
            db.commit()
            db.refresh(appraisalForm_object)

            db.query(Staff).filter(Staff.id == row.staff_id, Staff.supervisor_id == deadline.supervisor_id).update({
            Staff.appraisal_form_id : appraisalForm_object.id,
            }, synchronize_session=False)
            db.flush()
        
    db.commit()
    db.refresh(deadline_object)
    return "(" + str(deadline_object.deadline_type) + ") deadline created successfuly"











async def update_deadline(updateDeadline: UpdateDeadline, db:Session):
    deadline_id = updateDeadline.id
    is_mid_year_review_id_update = db.query(Deadline).filter(Deadline.id == deadline_id).update({
        Deadline.deadline_type : updateDeadline.deadline_type,
        Deadline.start_date : updateDeadline.start_date,
        Deadline.end_date : updateDeadline.end_date
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_mid_year_review_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Deadline with the id (" + str(deadline_id) + ") is not found")

    data = db.query(Deadline).filter(Deadline.id == deadline_id).one()
    return data