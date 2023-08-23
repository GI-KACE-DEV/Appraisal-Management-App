from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, crud
from  dependencies import get_db




# APIRouter creates path operations for mid_year_review module
mid_year_review_router = APIRouter()






@mid_year_review_router.post("/create")
async def create_new_mid_year_review(mid_year_review:schemas.CreateMidYearReview, db:Session = Depends(get_db)):

    return await crud.create_new_mid_year_review(mid_year_review=mid_year_review, db=db)











@mid_year_review_router.get("/id/{appraisal_form_id}")
async def staff_mid_year_review_form(appraisal_form_id: int, db:Session = Depends(get_db)):
    
    return await crud.staff_mid_year_review_form(appraisal_form_id, db)







@mid_year_review_router.put("/update")
async def update_mid_year_review(updateAppraisalForm: schemas.UpdateMidYearReview, db:Session = Depends(get_db)):
    
    return await crud.update_mid_year_review(updateAppraisalForm, db)








# @mid_year_review_router.delete("/deletemid_year_review/{id}")
# async def deletemid_year_review(id: int, db:Session = Depends(get_db)):
    
#     return await crud.deletemid_year_review(id, db)
