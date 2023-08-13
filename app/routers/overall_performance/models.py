from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text,TEXT
from sqlalchemy.orm import relationship
import datetime
import uuid
from database import Base


class OverallPerformance(Base):
    '''Overall Performance Model'''
    
    __tablename__ = "overall_performance"

    id = Column(String(255), primary_key=True,index=True, nullable=False, default=uuid.uuid4)
    description = Column(TEXT, nullable=True)
    performance = Column(TEXT, nullable=True)
    status = Column(Boolean, default=True, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
