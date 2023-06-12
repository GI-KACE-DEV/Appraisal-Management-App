#from routers.users.role.schemas import Role
from typing import Optional, List, Union
import routers.users.account.models as m
from pydantic import BaseModel, constr, EmailStr
#from constants import EMAIL, PHONE
import datetime, enum

class Account(str, enum.Enum):
    users = 'users'
    administrators = 'administrators'

class EmailBase(BaseModel):
    email: constr(regex='')
    
class PasswordBase(BaseModel):
    password: constr(min_length=8)

class UpdatePassword(PasswordBase):
    code: str
    password: constr(min_length=8)
    
class CreateAdmin(EmailBase):
    password: constr(min_length=8) = None
    

class Admin(EmailBase):
    id: int
    push_id: str
    is_active: bool
    created: datetime.datetime
    updated: datetime.datetime
    
    class Config:
        orm_mode = True

<<<<<<< HEAD
class CreateUser(EmailBase):
    username: str
=======
class CreateUser(BaseModel):
>>>>>>> 9133d4b8b4e7c88e9edc1c52c44eab3570720982
    email: EmailStr 
    is_active: bool
    staff_id: str
    password: constr(min_length=8) = None
    

class UpdateUser(BaseModel):
    email: EmailStr
    is_active: bool
    password: Optional[UpdatePassword]
    

class ShowUser(EmailBase):
    email : EmailStr 
    is_active : bool
 

    class Config:
        orm_mode = True



class User(EmailBase):
    id: int 
    email : EmailStr 
    is_active : bool
  

    class Config:
        orm_mode = True