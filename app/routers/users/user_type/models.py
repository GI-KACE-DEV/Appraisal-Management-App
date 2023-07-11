from sqlalchemy import Column, String, Integer
from database import Base
import re, uuid
from sqlalchemy.orm import Session

class UserType(Base):
    '''User Type Model'''

    __tablename__ = "user_type"

    id =Column(Integer,primary_key=True,index=True)
    title = Column(String(255), nullable=True)
