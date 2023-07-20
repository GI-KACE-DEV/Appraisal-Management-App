from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for performance_details module
performance_details_router = APIRouter()


@performance_details_router.post("/create", response_model=schemas.CreatePerformanceDetails)
async def create_new_performance_details(performance_details:schemas.CreatePerformanceDetails, db:Session = Depends(get_db)):

    return await crud.create_new_performance_details(performance_details=performance_details, db=db)







@performance_details_router.get("/all")
async def get_all_performance_details(db:Session = Depends(get_db)):

    return await crud.get_all_performance_details(db)






@performance_details_router.get("/id/{id}")
async def get_performance_details_By_Id(id: int, db:Session = Depends(get_db)):
    
    return await crud.get_performance_details_By_ID(id, db)







@performance_details_router.put("/update")
async def update_performance_details(updatePerformanceDetails: schemas.UpdatePerformanceDetails, db:Session = Depends(get_db)):
    
    return await crud.update_Performance_Details(updatePerformanceDetails, db)








# @performance_details_router.delete("/deleteperformance_details/{id}")
# async def deleteperformance_details(id: int, db:Session = Depends(get_db)):
    
#     return await crud.deleteperformance_details(id, db)
