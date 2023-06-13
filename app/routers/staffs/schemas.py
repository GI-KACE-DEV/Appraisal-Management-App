from typing import Optional
from pydantic import BaseModel, EmailStr

from datetime import date, datetime 

class BaseStaffDetails(BaseModel):
    email: EmailStr 
    

class CreateStaff(BaseStaffDetails):
    first_name: Optional[str]
    last_name: Optional[str]
    other_name: Optional[str]
    gender: Optional[str]
    supervisor_id: Optional[int]
    department: Optional[str]
    grade: Optional[int]
    is_active: bool
    is_superuser: bool 
    created_at: Optional[date] = datetime.now().date()
    updated_at: Optional[date] = datetime.now().date()

class ShowStaff(BaseStaffDetails):
    first_name: Optional[str]
    last_name: Optional[str]
    other_name: Optional[str]
    gender: Optional[str]
    supervisor_id: Optional[int]
    department: Optional[str]
    grade: Optional[int]
    is_active: bool
    is_superuser: bool 
 


    class Config():
        orm_model = True 


class UpdateStaff(BaseModel):
    #staff_id:Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    other_name: Optional[str]
    gender: Optional[str]
    #supervisor_id: Optional[int]
    department: Optional[str]
    grade: Optional[int]




    class Config():
        orm_model = True 

    