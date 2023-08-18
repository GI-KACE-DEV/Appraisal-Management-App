from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text,TEXT
from sqlalchemy.orm import relationship
import datetime
import uuid
from database import Base

class Comments(Base):
    '''Comments Model'''
    
    __tablename__ = "comments"

    id = Column(Integer,primary_key=True,index=True)
    first_phase = Column(TEXT, nullable=True)
    comment = Column(TEXT, nullable=True)
    supervisor_id = Column(Integer, ForeignKey("staffs.id"))
    appraisal_form_id = Column(Integer, ForeignKey("appraisal_forms.id"))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


    