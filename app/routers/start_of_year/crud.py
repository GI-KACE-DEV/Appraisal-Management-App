from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.start_of_year.schemas import CreateStartOfYear,UpdateStartOfYear
from routers.start_of_year.models import StartOfYear
from routers.appraisal_form.models import Appraisalview







async def create_new_start_of_year(start_of_year:CreateStartOfYear, db:Session):
    start_of_year_object = StartOfYear(**start_of_year.dict())
    
    db.add(start_of_year_object)
    db.flush()
    db.commit()
    db.refresh(start_of_year_object)
    return start_of_year_object









async def get_all_start_of_year(db:Session):
    data = db.query(StartOfYear).all()
    return data











async def staff_start_of_year_form(appraisal_form_id: int, db:Session):
    data = db.query(StartOfYear).filter(
        StartOfYear.appraisal_form_id == Appraisalview.appraisal_form_id,
        StartOfYear.appraisal_form_id == appraisal_form_id
        ).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Start Of Year form with the id {appraisal_form_id} is not found")
    return data








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

