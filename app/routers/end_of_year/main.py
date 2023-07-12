from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for end_of_year_review module
end_of_year_review_router = APIRouter()


@end_of_year_review_router.post("/create", response_model=schemas.CreateEndofYearReview)
async def create_new_end_of_year_review(end_of_year_review:schemas.CreateEndofYearReview, db:Session = Depends(get_db)):

    return await crud.create_new_end_of_year_review(end_of_year_review=end_of_year_review, db=db)







@end_of_year_review_router.get("/all")
async def get_all_end_of_year_review(db:Session = Depends(get_db)):

    return await crud.get_all_end_of_year_review(db)






@end_of_year_review_router.get("/getById/{id}")
async def get_end_of_year_review_By_Id(id: int, db:Session = Depends(get_db)):
    
    return await crud.get_end_of_year_review_By_ID(id, db)







@end_of_year_review_router.put("/update")
async def update_end_of_year_review(updateEndofYearReview: schemas.UpdateEndofYearReview, db:Session = Depends(get_db)):
    
    return await crud.update_End_of_Year_Review(updateEndofYearReview, db)








# @end_of_year_review_router.delete("/deleteend_of_year_review/{id}")
# async def deleteend_of_year_review(id: int, db:Session = Depends(get_db)):
    
#     return await crud.deleteend_of_year_review(id, db)
