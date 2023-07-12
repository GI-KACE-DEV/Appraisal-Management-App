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

    return await crud.create_new_staff_user(staff=staff, db=db)



## api route for getting returning all staff.
@staff_router.get("/getAllStaff")
async def get_all_staff(db:Session = Depends(get_db)):

    return await crud.get_all_staff(db)





# api route to get staff base on id. 
@staff_router.get("/getStaffById/{id}")
async def getStaffById(id: int, db:Session = Depends(get_db)):
  
    return await crud.getStaffById(id=id, db=db)







# api route to get staff base on email. 
@staff_router.get("/getStaffByEmail/{email}")
async def get_Staff_By_email(email: str, db:Session = Depends(get_db)):
  
    return await crud.get_Staff_By_email(email=email, db=db)






# api route to get staff base on token. 
@staff_router.get("/getAdminByToken/{token}")
async def get_Admin_By_Token(token: str, db:Session = Depends(get_db)):
  
    return await crud.get_Admin_By_Token(token=token, db=db)








# api route to update staff base on id.
@staff_router.put("/updateStaffAfterResetPassword")
async def update_Staff_After_Reset_Password(updateStaff: schemas.UpdateStaff, db:Session = Depends(get_db)):
    
    return await crud.update_Staff_After_Reset_Password(updateStaff, db)











# @staff_router.put("/updateStaff")
# async def updateStaff(updateStaff: schemas.UpdateStaff, db:Session = Depends(get_db)):
    
#     return await crud.updateStaff(updateStaff, db)



# @staff_router.delete("/deleteStaff/{id}")
# async def deleteStaff(id: int, db:Session = Depends(get_db)):
#     current_staff = 1
#     return await crud.deleteStaff(id=id, db=db, staff_id=current_staff)
