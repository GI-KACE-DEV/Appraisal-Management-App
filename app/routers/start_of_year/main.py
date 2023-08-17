from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from . import schemas, models, crud
from  dependencies import get_db
from routers.deadline.models import Deadline
import json
from routers.appraisal_form.models import AppraisalForm
from datetime import datetime




# APIRouter creates path operations for start_of_year module
start_of_year_router = APIRouter()


@start_of_year_router.post("/create")
async def create_new_start_of_year(start_of_year:schemas.CreateStartOfYear, db:Session = Depends(get_db)):

    return await crud.create_new_start_of_year(start_of_year=start_of_year, db=db)







# @start_of_year_router.get("/all")
# async def get_all_start_of_year(db:Session = Depends(get_db)):

#     return await crud.get_all_start_of_year(db)










@start_of_year_router.get("/id/{appraisal_form_id}")
async def get_staff_start_of_year_form(appraisal_form_id: int, db:Session = Depends(get_db)):
    
    return await crud.staff_start_of_year_form(appraisal_form_id, db)







@start_of_year_router.put("/update")
async def update_Start_Of_Year(updateStaff: schemas.UpdateStartOfYear, db:Session = Depends(get_db)):
    
    return await crud.updateStartOfYear(updateStaff, db)






@start_of_year_router.get("/testing/{appraisal_form_id}")
async def testing(appraisal_form_id: int, db:Session = Depends(get_db)):
    data = db.query(Deadline).filter(
        Deadline.deadline_type == "Start of Year",
        Deadline.supervisor_id == AppraisalForm.supervisor_id, 
        AppraisalForm.id == appraisal_form_id
        ).first()
    
    date = datetime.now()
    current_year = date.strftime("%Y")
    db_deadline_year = data.deadline_year

    # db_data ={
    #     "current_year": current_year,
    #     "deadline_year": data.deadline_year
    # }

    # return db_data

    if current_year == db_deadline_year:

       return "deadline year is (" + str(current_year) + ")"

    raise HTTPException(status_code=status.HTTP_303_SEE_OTHER,
            detail="deadline year does not match")








# @start_of_year_router.delete("/deletestart_of_year/{id}")
# async def deletestart_of_year(id: int, db:Session = Depends(get_db)):
    
#     return await crud.deletestart_of_year(id, db)
