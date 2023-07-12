import email
from typing import Optional
from pydantic import BaseModel, EmailStr

from datetime import date, datetime 


    
class CreateStaff(BaseModel):
    email: EmailStr 
    first_name: Optional[str]
    last_name: Optional[str]
    other_name: Optional[str]
    gender: Optional[str]
    supervisor_id: Optional[int]
    department: Optional[str]
    positions: Optional[str]
    appointment_date: Optional[str]
    grade: Optional[int]
    user_type_id: Optional[int]
    is_active: bool
    is_superuser: bool 


class ShowStaff(BaseModel):
    # email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    other_name: Optional[str]
    gender: Optional[str]
    supervisor_id: Optional[int]
    department: Optional[str]
    grade: Optional[int]
   
 
    class Config():
        orm_mode = True 


class UpdateStaff(BaseModel):
    id:Optional[int]
    email: EmailStr 
    first_name: Optional[str]
    last_name: Optional[str]
    other_name: Optional[str]
    gender: Optional[str]
    supervisor_id: Optional[int]
    department: Optional[str]
    positions: Optional[str]
    appointment_date: Optional[str]
    grade: Optional[int]
    hashed_password: Optional[str]
    user_type_id: Optional[int]
    is_active: bool
    is_superuser: bool 


    class Config():
        orm_mode = True 






# class ShowAppraisalView(BaseModel):
#     staff_id: Optional[str]
#     email: EmailStr 
#     first_name: Optional[str]
#     last_name: Optional[str]
#     other_name: Optional[str]
#     gender: Optional[str]
#     supervisor_id: Optional[int]
#     department: Optional[str]
#     positions: Optional[str]
#     grade: Optional[int]
#     is_active: bool
#     is_superuser: bool 