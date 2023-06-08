from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
from sqlalchemy.orm import relationship

from database import Base


class Staff(Base):
    '''Staff Model'''
    
    __tablename__ = "staff"
    staff_id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    other_name = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    supervisor_id = Column(Integer, nullable=True)
    department = Column(String, nullable=True)
    grade = Column(Integer, nullable=True)
    date_joined = Column(Date, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    status = None 