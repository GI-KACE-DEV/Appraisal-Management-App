from fastapi import APIRouter, Depends, Form, status
from typing import List
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for staffs module
staff_router = APIRouter()

@staff_router.post("/create", response_model=schemas.ShowStaff)
async def create_staff_user(staff: schemas.CreateStaff, db: Session = Depends(get_db)):
    staff = crud.create_new_staff_user(staff=staff, db=db)

    return staff

# @staff_router.post("/create", response_description="Staff data added into the database")
# async def create_new_satff( db:Session = Depends(get_db), first_name:str = Form(...), last_name:str = Form(...),
#                 other_name:str = Form(None), email:str = Form(...),
#                 gender:str = Form(None) ,department:str = Form(None),
#                 grade:str = Form(None), supervisor_id:str = Form(None)):
    
#     return await crud.create_new_satff(db, first_name, last_name, other_name,email,gender,
#                                        department, grade, supervisor_id)

## api route for getting returning all staff.
@staff_router.get("/getAllStaff", response_model=List[schemas.ShowStaff])
async def get_all_staff(db:Session = Depends(get_db)):

    return await crud.get_all_staff(db)


# api route to get staff base on id. 
@staff_router.get("/getStaffById/{id}", response_model=schemas.ShowStaff)
async def getStaffById(id: int, db:Session = Depends(get_db)):
    # staff = crud.getStaffById(id=id, db=db)
    
    return await crud.getStaffById(id=id, db=db)


# @staff_router.put("/updateStaff")
# async def updateStaff(updateStaff: schemas.UpdateStaff, db:Session = Depends(get_db)):
    
#     return await crud.updateStaff(updateStaff, db)



# @staff_router.delete("/deleteStaff/{id}")
# async def deleteStaff(id: int, db:Session = Depends(get_db)):
    
#     return await crud.deleteStaff(id, db)
