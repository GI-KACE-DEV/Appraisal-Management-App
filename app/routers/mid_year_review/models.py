from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text,TEXT
from sqlalchemy.orm import relationship
import datetime

from database import Base


class MidYearReview(Base):
    '''Mid of Year Review Model'''
    
    __tablename__ = "mid_year_review"

    id = Column(Integer,primary_key=True,index=True)
    progress_review = Column(TEXT, nullable=True)
    remarks = Column(TEXT, nullable=True)
    competency = Column(TEXT, nullable=True)
    appraisal_form_id = Column(Integer, ForeignKey("appraisal_forms.id"))
    deadline_start_date = Column(String(255), nullable=True)
    deadline_end_date = Column(String(255), nullable=True)
    mid_status = Column(Boolean, default=True, nullable=True)
    submit = Column(Boolean, default=False, nullable=True)
    mid_year_review_status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
