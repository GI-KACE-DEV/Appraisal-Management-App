from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime 


class CreateDeadline(BaseModel):
    deadline_type: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    departmental_id: Optional[str]
    

    class Config():
        orm_model = True 




class UpdateDeadline(BaseModel):
    id:Optional[str]
    departmental_id:Optional[str]
    comment: Optional[str]




    class Config():
        orm_model = True 
    