from fastapi import APIRouter, Depends, Form, status
from typing import List
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db 

from routers.users.account.models import User




# APIRouter creates path operations for staffs module
staff_router = APIRouter()

@staff_router.post("/create", response_model=schemas.ShowStaff)
async def create_staff_user(staff: schemas.CreateStaff, db: Session = Depends(get_db)):

    staff = crud.create_new_staff_user(staff=staff, db=db)
    return staff



## api route for getting returning all staff.
@staff_router.get("/getAllStaff", response_model=List[schemas.ShowStaff])
async def get_all_staff(db:Session = Depends(get_db)):

    return await crud.get_all_staff(db)


# api route to get staff base on id. 
@staff_router.get("/getStaffById/{id}", response_model=schemas.ShowStaff)
async def getStaffById(id: int, db:Session = Depends(get_db)):
  
    return await crud.getStaffById(id=id, db=db)


# @staff_router.put("/updateStaff")
# async def updateStaff(updateStaff: schemas.UpdateStaff, db:Session = Depends(get_db)):
    
#     return await crud.updateStaff(updateStaff, db)



# @staff_router.delete("/deleteStaff/{id}")
# async def deleteStaff(id: int, db:Session = Depends(get_db)):
#     current_staff = 1
#     return await crud.deleteStaff(id=id, db=db, staff_id=current_staff)
