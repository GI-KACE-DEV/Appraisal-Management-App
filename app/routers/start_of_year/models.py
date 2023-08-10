from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text,TEXT
from sqlalchemy.orm import relationship
import datetime

from database import Base


class StartOfYear(Base):
    '''Start of Year Model'''
    
    __tablename__ = "start_of_year"

    id = Column(Integer,primary_key=True,index=True)
    first_phase = Column(TEXT, nullable=True)
    # target = Column(TEXT, nullable=True)
    # resources = Column(String(255), nullable=True)
    appraisal_form_id = Column(Integer, ForeignKey("appraisal_forms.id"))
    deadline_start_date = Column(String(255), nullable=True)
    deadline_end_date = Column(String(255), nullable=True)
    start_status = Column(Boolean, default=True, nullable=True)
    submit_status = Column(Boolean, default=False, nullable=True)
    approval_status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
