from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateStartOfYear(BaseModel):
    results_areas: Optional[str]
    target: Optional[str]
    resources: Optional[str]
    appraisal_form_id: Optional[int]
    status: bool
    



class ShowStartOfYear(BaseModel):
    results_areas: Optional[str]
    target: Optional[str]
    resources: Optional[str]


    class Config():
        orm_mode = True



class UpdateStartOfYear(BaseModel):
    appraisal_form_id:Optional[int]
    department: Optional[str]
    grade: Optional[str]
    positions: Optional[str]
    appraisal_date: Optional[str]




    class Config():
        orm_model = True 
    