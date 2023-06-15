from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateAppraisalForm(BaseModel):
    department: Optional[str]
    grade: Optional[str]
    positions: Optional[str]
    appraisal_date: Optional[str]
    status: bool
    created_at: Optional[date] = datetime.now().date()
    updated_at: Optional[date] = datetime.now().date()
    



class ShowAppraisalForm(BaseModel):
    department: Optional[str]
    grade: Optional[str]
    positions: Optional[str]


    class Config():
        orm_mode = True



class UpdateAppraisalForm(BaseModel):
    appraisal_form_id:Optional[int]
    department: Optional[str]
    grade: Optional[str]
    positions: Optional[str]
    appraisal_date: Optional[str]




    class Config():
        orm_model = True 
    