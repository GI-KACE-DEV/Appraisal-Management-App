from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for start_of_year module
start_of_year_router = APIRouter()


@start_of_year_router.post("/create")
async def create_new_start_of_year(start_of_year:schemas.CreateStartOfYear, db:Session = Depends(get_db)):

    return await crud.create_new_start_of_year(start_of_year=start_of_year, db=db)







# @start_of_year_router.get("/all")
# async def get_all_start_of_year(db:Session = Depends(get_db)):

#     return await crud.get_all_start_of_year(db)










@start_of_year_router.get("/id/{appraisal_form_id}")
async def get_staff_start_of_year_form(appraisal_form_id: str, db:Session = Depends(get_db)):
    
    return await crud.staff_start_of_year_form(appraisal_form_id, db)







@start_of_year_router.put("/update")
async def update_Start_Of_Year(updateStaff: schemas.UpdateStartOfYear, db:Session = Depends(get_db)):
    
    return await crud.updateStartOfYear(updateStaff, db)








# @start_of_year_router.delete("/deletestart_of_year/{id}")
# async def deletestart_of_year(id: str, db:Session = Depends(get_db)):
    
#     return await crud.deletestart_of_year(id, db)
