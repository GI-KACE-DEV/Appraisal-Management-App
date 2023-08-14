from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for overall_performance module
overall_performance_router = APIRouter()


@overall_performance_router.post("/create")
async def create_new_overall_performance(overall_performance:schemas.CreateOverallPerformance, db:Session = Depends(get_db)):

    return await crud.create_new_overall_performance(overall_performance=overall_performance, db=db)







@overall_performance_router.get("/all")
async def get_all_overall_performance(db:Session = Depends(get_db)):

    return await crud.get_all_overall_performance(db)






@overall_performance_router.get("/id/{id}")
async def get_overall_performance_By_Id(id: int, db:Session = Depends(get_db)):
    
    return await crud.get_overall_performance_By_ID(id, db)







@overall_performance_router.put("/update")
async def update_overall_performance(updateOverallPerformance: schemas.UpdateOverallPerformance, db:Session = Depends(get_db)):
    
    return await crud.update_Overall_Performance(updateOverallPerformance, db)








# @overall_performance_router.delete("/deleteoverall_performance/{id}")
# async def deleteoverall_performance(id: int, db:Session = Depends(get_db)):
    
#     return await crud.deleteoverall_performance(id, db)
