from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateComments(BaseModel):
    comment: Optional[str]
    appraisal_form_id: Optional[int]
    

    class Config():
        orm_model = True 




class UpdateComments(BaseModel):
    id:Optional[str]
    appraisal_form_id:Optional[int]
    comment: Optional[str]




    class Config():
        orm_model = True 
    