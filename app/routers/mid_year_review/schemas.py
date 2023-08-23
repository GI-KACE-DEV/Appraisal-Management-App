from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateMidYearReview(BaseModel):
    progress_review: Optional[str]
    remarks: Optional[str]
    competency: Optional[str]
    appraisal_form_id: Optional[int]
    submit_status: Optional[bool] = False
    




    class Config():
        orm_mode = True



class UpdateMidYearReview(BaseModel):
    id:Optional[int]
    progress_review: Optional[str]
    remarks: Optional[str]
    competency: Optional[str]
    appraisal_form_id: Optional[int]
    approval_status: Optional[bool]




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