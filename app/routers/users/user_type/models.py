from sqlalchemy import Column, String, Integer
#from mixins import BaseMixin, HashMethodMixin
from sqlalchemy.orm import validates
#from constants import PHONE, EMAIL
from utils import gen_code
from database import Base
import re, uuid

class UserType(Base):
    '''User Type Model'''

    __tablename__ = "user-type"

    usertype_id =Column(Integer,primary_key=True,index=True)
    title = Column(String, nullable=True)


    status = None