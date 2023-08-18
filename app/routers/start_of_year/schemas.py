from typing import Optional, Any
from pydantic import BaseModel

from datetime import date, datetime 


class CreateStartOfYear(BaseModel):
    first_phase: Any
    appraisal_form_id: Optional[int]
    submit_status: Optional[bool] = False
    





class ShowStartOfYear(BaseModel):
    results_areas: Optional[str]
    target: Optional[str]
    resources: Optional[str]


    class Config():
        orm_mode = True



class UpdateStartOfYear(BaseModel):
    id: int
    first_phase: Any
    appraisal_form_id: Optional[int]
    approval_status: Optional[bool]
    comment: Optional[str]




    class Config():
        orm_model = True 
    











class UpdateStaffDeadline(BaseModel):
    id:Optional[int]
    deadline_type: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    appraisal_form_id: Optional[int]
    supervisor_id: Optional[int]
    comment: str




    class Config():
        orm_model = True 