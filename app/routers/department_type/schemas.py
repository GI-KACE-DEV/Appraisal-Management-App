from typing import Optional 

from pydantic import BaseModel

class DepTypeBase(BaseModel):
    title: Optional[str] = None 

class CreateDepType(DepTypeBase):
    title: str 

class ShowDepType(DepTypeBase):
    title: str 

    class Config():
        orm_mode = True 

class UpdateDepType(DepTypeBase):
    pass 

class DeleteDepType(DepTypeBase):
    pass 