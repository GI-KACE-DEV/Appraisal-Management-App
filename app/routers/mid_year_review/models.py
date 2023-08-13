from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text,TEXT
from sqlalchemy.orm import relationship
import datetime
import uuid
from database import Base


class MidYearReview(Base):
    '''Mid of Year Review Model'''
    
    __tablename__ = "mid_year_review"

    id = Column(String(255), primary_key=True,index=True, nullable=False, default=uuid.uuid4)
    progress_review = Column(TEXT, nullable=True)
    remarks = Column(TEXT, nullable=True)
    competency = Column(TEXT, nullable=True)
    appraisal_form_id = Column(String(255), ForeignKey("appraisal_forms.id"))
    deadline_start_date = Column(String(255), nullable=True)
    deadline_end_date = Column(String(255), nullable=True)
    mid_status = Column(Boolean, default=True, nullable=True)
    submit = Column(Boolean, default=False, nullable=True)
    approval_status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
