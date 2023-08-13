from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text,TEXT, DateTime
from sqlalchemy.orm import relationship
import uuid
from database import Base


class Deadline(Base):
    '''Deadline Model'''
    
    __tablename__ = "deadline"

    id = Column(String(255), primary_key=True,index=True, nullable=False, default=uuid.uuid4)
    deadline_type = Column(String(255), nullable=True)
    start_date = Column(String(255), nullable=True)
    end_date = Column(String(255), nullable=True)
    appraisal_form_id = Column(String(255), ForeignKey("appraisal_forms.id"))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
