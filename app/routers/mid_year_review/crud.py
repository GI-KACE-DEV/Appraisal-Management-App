from routers.mid_year_review.schemas import CreateMidYearReview,UpdateMidYearReview,UpdateStaffDeadline
from routers.mid_year_review.models import MidYearReview
from routers.appraisal_form.models import AppraisalForm
from routers.deadline.models import StaffDeadline
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from routers.staffs.models import Staff 
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import status
import json










async def create_new_mid_year_review(mid_year_review:CreateMidYearReview, db:Session):
    data = db.query(StaffDeadline).filter(
        StaffDeadline.deadline_type == "Mid",
        StaffDeadline.supervisor_id == AppraisalForm.supervisor_id,
        StaffDeadline.appraisal_form_id == mid_year_review.appraisal_form_id
        ).first()
    year = datetime.now()
    current_year = year.strftime("%Y")
    date_str = year.strftime("%m/%d/%Y")
    start_date = data.start_date
    end_date = data.end_date
    db_deadline_year = data.deadline_year

    if current_year == db_deadline_year and date_str >= start_date and date_str <= end_date:
        mid_year_review_object = MidYearReview(**mid_year_review.dict())
        db.add(mid_year_review_object)
        db.flush()
        db.commit()
        db.refresh(mid_year_review_object)
        return "mid of year added successfully"
    
    raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
            detail="please contact your supervisor for more info")














async def get_all_mid_year_review(db:Session):
    data = db.query(MidYearReview).all()
    return data






async def staff_mid_year_review_form(appraisal_form_id: int, db:Session):
    data = db.query(MidYearReview).filter(
        MidYearReview.appraisal_form_id == Staff.appraisal_form_id,
        MidYearReview.appraisal_form_id == appraisal_form_id
        ).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Mid Year Review form with the id {appraisal_form_id} is not found")
    return data








async def update_mid_year_review(updateMidYearReview: UpdateMidYearReview, db:Session):
    mid_year_review_id = updateMidYearReview.id
    is_mid_year_review_id_update = db.query(MidYearReview).filter(MidYearReview.id == mid_year_review_id).update({
        MidYearReview.progress_review : updateMidYearReview.progress_review,
        MidYearReview.competency : updateMidYearReview.competency,
        MidYearReview.remarks : updateMidYearReview.remarks,
        MidYearReview.approval_status : updateMidYearReview.approval_status
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_mid_year_review_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Mid Year Review with the id (" + str(mid_year_review_id) + ") is not found")

    data = db.query(MidYearReview).filter(MidYearReview.id == mid_year_review_id).one()
    return data










async def deleteAppraisalForm(id: int, db:Session):
    db_data = db.query(MidYearReview).filter(MidYearReview.id == id).update({
            MidYearReview.status: 0
            }, synchronize_session=False)
    db.flush()
    db.commit()
    if not db_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"MidYearReview with the id {id} is not found")

    data = db.query(MidYearReview).filter(MidYearReview.id == id).one()
    return data

