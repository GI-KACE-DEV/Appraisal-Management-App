from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for start_of_year module
start_of_year_router = APIRouter()


@start_of_year_router.post("/create", response_model=schemas.ShowStartOfYear)
async def create_new_start_of_year(start_of_year:schemas.CreateStartOfYear, db:Session = Depends(get_db)):

    return await crud.create_new_start_of_year(start_of_year=start_of_year, db=db)







# @start_of_year_router.get("/get_start_of_year")
# async def get_all_start_of_year(db:Session = Depends(get_db)):

#     return await crud.get_all_start_of_year(db)






# @start_of_year_router.get("/getstart_of_yearById/{id}")
# async def getstart_of_yearById(id: int, db:Session = Depends(get_db)):
    
#     return await crud.get_start_of_yearBy_ID(id, db)







# @start_of_year_router.put("/updatestart_of_year")
# async def updatestart_of_year(updateStaff: schemas.Updatestart_of_year, db:Session = Depends(get_db)):
    
#     return await crud.updatestart_of_year(updateStaff, db)








# @start_of_year_router.delete("/deletestart_of_year/{id}")
# async def deletestart_of_year(id: int, db:Session = Depends(get_db)):
    
#     return await crud.deletestart_of_year(id, db)
