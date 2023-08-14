from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateMidYearReview(BaseModel):
    progress_review: Optional[str]
    remarks: Optional[str]
    competency: Optional[str]
    appraisal_form_id: Optional[int]
    




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
    