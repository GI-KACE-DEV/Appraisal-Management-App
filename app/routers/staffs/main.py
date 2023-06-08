from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for staffs module
staff_router = APIRouter()


@staff_router.post("/create", response_description="Staff data added into the database")
async def create_new_satff(staff:schemas.CreateStaff, db:Session = Depends(get_db)):
    
    return await crud.create_new_satff(staff, db)


@staff_router.get("/getAllStaff")
async def get_all_staff(db:Session = Depends(get_db)):

    return await crud.get_all_staff(db)



@staff_router.get("/getStaffById/{id}")
async def getStaffById(id: int, db:Session = Depends(get_db)):
    
    return await crud.getStaffById(id, db)


@staff_router.put("/updateStaff")
async def updateStaff(updateStaff: schemas.UpdateStaff, db:Session = Depends(get_db)):
    
    return await crud.updateStaff(updateStaff, db)



@staff_router.delete("/deleteStaff/{id}")
async def deleteStaff(id: int, db:Session = Depends(get_db)):
    
    return await crud.deleteStaff(id, db)
