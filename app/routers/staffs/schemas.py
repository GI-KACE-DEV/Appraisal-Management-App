from typing import Optional
from pydantic import BaseModel



class CreateStaff(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    other_name: Optional[str]
    gender: Optional[str]
    supervisor_id: Optional[int]
    department: Optional[str]
    grade: Optional[int]



    class Config():
        orm_model = True


class UpdateStaff(BaseModel):
    staff_id:Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    other_name: Optional[str]
    gender: Optional[str]
    supervisor_id: Optional[int]
    department: Optional[str]
    grade: Optional[int]




    class Config():
        orm_model = True 
    