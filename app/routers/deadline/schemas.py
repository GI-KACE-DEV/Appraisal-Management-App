from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime 


class CreateDeadline(BaseModel):
    deadline_type: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    supervisor_id: Optional[int]
    

    class Config():
        orm_model = True 




class UpdateDeadline(BaseModel):
    id:Optional[int]
    deadline_type: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    supervisor_id: Optional[int]




    class Config():
        orm_model = True 
    