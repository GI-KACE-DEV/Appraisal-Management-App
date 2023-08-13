from sqlalchemy import Column, String, Integer
from database import Base
import re, uuid
from sqlalchemy.orm import Session

class UserType(Base):
    '''User Type Model'''

    __tablename__ = "user_type"

    id =Column(String(255), primary_key=True,index=True, nullable=False, default=uuid.uuid4)
    title = Column(String(255), nullable=True)
