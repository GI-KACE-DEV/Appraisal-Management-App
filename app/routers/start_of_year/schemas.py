from typing import Optional, Any
from pydantic import BaseModel

from datetime import date, datetime 


class CreateStartOfYear(BaseModel):
    first_phase: Any
    # target: Optional[str]
    # resources: Optional[str]
    appraisal_form_id: Optional[int]
    submit_status: Optional[bool] = False
    





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
    approval_status: Optional[bool]




    class Config():
        orm_model = True 
    