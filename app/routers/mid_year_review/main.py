from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for mid_year_review module
mid_year_review_router = APIRouter()


@mid_year_review_router.post("/create")
async def create_new_mid_year_review(mid_year_review:schemas.CreateMidYearReview, db:Session = Depends(get_db)):

    return await crud.create_new_mid_year_review(mid_year_review=mid_year_review, db=db)







@mid_year_review_router.get("/all")
async def get_all_mid_year_review(db:Session = Depends(get_db)):

    return await crud.get_all_mid_year_review(db)






@mid_year_review_router.get("/getById/{id}")
async def get_mid_year_review_By_Id(id: int, db:Session = Depends(get_db)):
    
    return await crud.get_mid_year_review_By_ID(id, db)







# @mid_year_review_router.put("/update")
# async def updateMidYearReview(updateAppraisalForm: schemas.UpdateMidYearReview, db:Session = Depends(get_db)):
    
#     return await crud.update_Appraisal_Form(updateAppraisalForm, db)








# @mid_year_review_router.delete("/deletemid_year_review/{id}")
# async def deletemid_year_review(id: int, db:Session = Depends(get_db)):
    
#     return await crud.deletemid_year_review(id, db)
