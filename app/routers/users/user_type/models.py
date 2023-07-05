from sqlalchemy import Column, String, Integer
from database import Base
import re, uuid

class UserType(Base):
    '''User Type Model'''

    __tablename__ = "user_type"

    usertype_id =Column(Integer,primary_key=True,index=True)
    title = Column(String(255), nullable=True)


    status = None