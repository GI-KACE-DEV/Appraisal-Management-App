from typing import Optional
from pydantic import BaseModel



class CreateAppraisalForm(BaseModel):
    department: Optional[str]
    grade: Optional[str]
    positions: Optional[str]
    appraisal_date: Optional[str]
    #staff_id: Optional[int]




    class Config():
        orm_model = True


class UpdateAppraisalForm(BaseModel):
    appraisal_form_id:Optional[int]
    department: Optional[str]
    grade: Optional[str]
    positions: Optional[str]
    appraisal_date: Optional[str]




    class Config():
        orm_model = True 
    