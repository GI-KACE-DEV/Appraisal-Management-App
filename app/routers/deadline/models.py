from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text,TEXT, DateTime
from sqlalchemy.orm import relationship
import uuid
from database import Base


class DepartmentDeadline(Base):
    '''Department Deadline Model'''
    
    __tablename__ = "department_deadline"

    id = Column(Integer,primary_key=True,index=True)
    deadline_type = Column(String(255), nullable=True)
    start_date = Column(String(255), nullable=True)
    end_date = Column(String(255), nullable=True)
    deadline_year = Column(String(255), nullable=True)
    supervisor_id = Column(Integer, ForeignKey("staffs.id"))
    comment = Column(TEXT, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))









class StaffDeadline(Base):
    '''Staff Deadline Model'''
    
    __tablename__ = "staff_deadline"

    id = Column(Integer,primary_key=True,index=True)
    deadline_type = Column(String(255), nullable=True)
    start_date = Column(String(255), nullable=True)
    comment = Column(TEXT, nullable=True)
    end_date = Column(String(255), nullable=True)
    deadline_year = Column(String(255), nullable=True)
    appraisal_form_id = Column(Integer, ForeignKey("appraisal_forms.id"))
    supervisor_id = Column(Integer, ForeignKey("staffs.id"))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))