from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateMidYearReview(BaseModel):
    progress_review: Optional[str]
    remarks: Optional[str]
    competency: Optional[str]
    appraisal_form_id: Optional[int]
    



class ShowMidYearReview(BaseModel):
    results_areas: Optional[str]
    target: Optional[str]
    resources: Optional[str]


    class Config():
        orm_mode = True



class UpdateMidYearReview(BaseModel):
    appraisal_form_id:Optional[int]
    department: Optional[str]
    grade: Optional[str]
    positions: Optional[str]
    appraisal_date: Optional[str]




    class Config():
        orm_model = True 
    