from routers.start_of_year.schemas import CreateStartOfYear,UpdateStartOfYear,UpdateStaffDeadline
from routers.appraisal_form.models import AppraisalForm
from routers.start_of_year.models import StartOfYear
from routers.deadline.models import StaffDeadline
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from routers.staffs.models import Staff 
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import status
import json









async def create_new_start_of_year(start_of_year:CreateStartOfYear, db:Session):

    data = db.query(StaffDeadline).filter(
        StaffDeadline.deadline_type == "Start of Year",
        StaffDeadline.supervisor_id == AppraisalForm.supervisor_id,
        StaffDeadline.appraisal_form_id == start_of_year.appraisal_form_id
        ).first()
    
    year = datetime.now()
    current_year = year.strftime("%Y")
    date_str = year.strftime("%m/%d/%Y")
    start_date = data.start_date
    end_date = data.end_date
    db_deadline_year = data.deadline_year

    if current_year == db_deadline_year and date_str >= start_date and date_str <= end_date:
        json_data = jsonable_encoder({key: item for key, item in enumerate(start_of_year.first_phase)})
        #json_data = jsonable_encoder(start_of_year.first_phase)
        start_of_year_object = StartOfYear()
        start_of_year_object.first_phase = json.dumps(json_data)
        start_of_year_object.deadline_start_date = data.start_date
        start_of_year_object.deadline_end_date = data.end_date
        start_of_year_object.appraisal_form_id = start_of_year.appraisal_form_id
        start_of_year_object.submit_status = start_of_year.submit_status
        db.add(start_of_year_object)
        db.flush()
        db.commit()
        db.refresh(start_of_year_object)
        return "start of year added successfully"
    
    raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
            detail="please contact your supervisor for more info")









async def get_all_start_of_year(db:Session):
    data = db.query(StartOfYear).all()
    return data









async def staff_start_of_year_form(appraisal_form_id: int, db:Session):
    data = db.query(StartOfYear).filter(
        StartOfYear.appraisal_form_id == Staff.appraisal_form_id,
        StartOfYear.appraisal_form_id == appraisal_form_id
        ).first()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Start Of Year form with the id {appraisal_form_id} is not found")
    
    first_phase = json.loads(data.first_phase)

    db_data = {
            "id": data.id,
            "appraisal_form_id": data.appraisal_form_id,
            "submit_status": data.submit_status,
            "first_phase": first_phase
    }
    return db_data








async def update_start_of_year(updateStartOfYear: UpdateStartOfYear, db:Session):
    db_id = updateStartOfYear.id
    json_data = jsonable_encoder({key: item for key, item in enumerate(updateStartOfYear.first_phase)})
    year = datetime.now()
    approval_date = year.strftime("%m/%d/%Y %H:%M:%S")
    is_db_id_update = db.query(StartOfYear).filter(StartOfYear.id == db_id).update({
        StartOfYear.first_phase : json.dumps(json_data),
        StartOfYear.appraisal_form_id : updateStartOfYear.appraisal_form_id,
        StartOfYear.approval_status : updateStartOfYear.approval_status,
        StartOfYear.comment : updateStartOfYear.comment,
        StartOfYear.approval_date : approval_date
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_db_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Start Of Year with the id (" + str(db_id) + ") is not found")

    data = db.query(StartOfYear).filter(StartOfYear.id == db_id).one()
    return data













async def get_start_deadline(appraisal_form_id: int, db:Session):
    data = db.query(StaffDeadline).filter(
        StaffDeadline.appraisal_form_id == Staff.appraisal_form_id,
        StaffDeadline.appraisal_form_id == appraisal_form_id
        ).first()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Staff Deadline with the id {appraisal_form_id} is not found")

    return data

















async def update_start_deadline(update_start_deadline: UpdateStaffDeadline, db:Session):
    deadline_id = update_start_deadline.appraisal_form_id
    is_mid_year_review_id_update = db.query(StaffDeadline).filter(StaffDeadline.appraisal_form_id == deadline_id).update({
        StaffDeadline.deadline_type : update_start_deadline.deadline_type,
        StaffDeadline.start_date : update_start_deadline.start_date,
        StaffDeadline.appraisal_form_id : update_start_deadline.appraisal_form_id,
        StaffDeadline.supervisor_id : update_start_deadline.supervisor_id,
        StaffDeadline.end_date : update_start_deadline.end_date,
        StaffDeadline.comment : update_start_deadline.comment
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_mid_year_review_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff Deadline with the id (" + str(deadline_id) + ") is not found")

    data = db.query(StaffDeadline).filter(StaffDeadline.appraisal_form_id == deadline_id).one()
    return data








# async def deleteStartOfYear(id: int, db:Session):
#     db_data = db.query(StartOfYear).filter(StartOfYear.id == id).update({
#             StartOfYear.status: 0
#             }, synchronize_session=False)
#     db.flush()
#     db.commit()
#     if not db_data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"StartOfYear with the id {id} is not found")

#     data = db.query(StartOfYear).filter(StartOfYear.id == id).one()
#     return data

