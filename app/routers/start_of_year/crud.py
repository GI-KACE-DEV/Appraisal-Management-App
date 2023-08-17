from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.start_of_year.schemas import CreateStartOfYear,UpdateStartOfYear
from routers.start_of_year.models import StartOfYear
from routers.appraisal_form.models import Appraisalview
from routers.staffs.models import Staff 
from fastapi.encoders import jsonable_encoder
from routers.deadline.models import Deadline
import json
from routers.appraisal_form.models import AppraisalForm
from datetime import datetime
from sqlalchemy import or_






async def create_new_start_of_year(start_of_year:CreateStartOfYear, db:Session):

    data = db.query(Deadline).filter(
        Deadline.deadline_type == "Start of Year",
        Deadline.supervisor_id == AppraisalForm.supervisor_id,
        AppraisalForm.id == start_of_year.appraisal_form_id).first()
    
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
            "first_phase": first_phase,
            "appraisal_form_id": data.appraisal_form_id,
            "submit_status": data.submit_status
    }
    return db_data








async def updateStartOfYear(updateStartOfYear: UpdateStartOfYear, db:Session):
    start_of_year_id = updateStartOfYear.id
    is_start_of_year_id_update = db.query(StartOfYear).filter(StartOfYear.id == start_of_year_id).update({
        StartOfYear.results_areas : updateStartOfYear.results_areas,
        StartOfYear.target : updateStartOfYear.target,
        StartOfYear.resources : updateStartOfYear.resources,
        StartOfYear.approval_status : updateStartOfYear.approval_status
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_start_of_year_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Start Of Year with the id (" + str(start_of_year_id) + ") is not found")

    data = db.query(StartOfYear).filter(StartOfYear.id == start_of_year_id).one()
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

