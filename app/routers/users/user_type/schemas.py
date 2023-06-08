#from routers.users.role.schemas import Role
from typing import Optional, List, Union
import routers.users.account.models as m
from pydantic import BaseModel, constr, EmailStr
#from constants import EMAIL, PHONE
import datetime, enum

class CreateUserType(BaseModel):
    id: int
    title: str

class ShowUserType(BaseModel):
    title: str

    class Config:
        orm_model = True