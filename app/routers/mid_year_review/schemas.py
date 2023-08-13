from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateMidYearReview(BaseModel):
    progress_review: Optional[str]
    remarks: Optional[str]
    competency: Optional[str]
    appraisal_form_id: Optional[str]
    




    class Config():
        orm_mode = True



class UpdateMidYearReview(BaseModel):
    id:Optional[str]
    progress_review: Optional[str]
    remarks: Optional[str]
    competency: Optional[str]
    appraisal_form_id: Optional[str]
    approval_status: Optional[bool]




    class Config():
        orm_model = True 
    