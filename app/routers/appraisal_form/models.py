from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
import datetime
from sqlalchemy.orm import relationship
import uuid
from database import Base
from sqlalchemy.dialects.postgresql import UUID



class AppraisalForm(Base):
    '''Appraisal Form Model'''
    
    __tablename__ = "appraisal_forms"

    id = Column(Integer,primary_key=True,index=True)
    department = Column(String(255), nullable=True)
    grade = Column(String(255), nullable=True)
    positions = Column(String(255), nullable=True)
    appraisal_year = Column(String(255), nullable=True)
    staff_id = Column(Integer, ForeignKey("staffs.id"))
    supervisor_id = Column(Integer, ForeignKey("staffs.id"))
    status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

