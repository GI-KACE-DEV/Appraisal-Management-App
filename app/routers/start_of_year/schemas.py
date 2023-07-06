from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateStartOfYear(BaseModel):
    results_areas: Optional[str]
    target: Optional[str]
    resources: Optional[str]
    appraisal_form_id: Optional[int]
    



class ShowStartOfYear(BaseModel):
    results_areas: Optional[str]
    target: Optional[str]
    resources: Optional[str]


    class Config():
        orm_mode = True



class UpdateStartOfYear(BaseModel):
    id:Optional[int]
    appraisal_form_id:Optional[int]
    results_areas: Optional[str]
    target: Optional[str]
    resources: Optional[str]
    appraisal_date: Optional[str]




    class Config():
        orm_model = True 
    