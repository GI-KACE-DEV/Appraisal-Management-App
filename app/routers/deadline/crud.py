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
from datetime import datetime




async def create_deadline(deadline:CreateDeadline, db: Session):
    deadline_object = Deadline(**deadline.dict())
    db.add(deadline_object)
    db.flush()

    today = datetime.now()

    db_data = db.query(Appraisalview).filter(Appraisalview.supervisor_id == deadline.staff_id).all()

    if not db_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Staff with the id {deadline.staff_id} is not found")

    if deadline.deadline_type == "Start of Year" or deadline.deadline_type == "First Phase":
        appraisalForm_object = AppraisalForm(appraisal_year = today.year, department = db_data.department,
                            grade = db_data.grade, positions = db_data.positions,  staff_id=deadline.staff_id)
    
    db.add(appraisalForm_object)
    db.flush()
    db.commit()
    db.refresh(deadline_object)
    db.refresh(appraisalForm_object)
    return deadline_object











