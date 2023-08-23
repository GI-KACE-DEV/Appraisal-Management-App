from sqlalchemy import Column, String, event, TIMESTAMP
from sqlalchemy.orm import validates 
from ..account.models import *
from constants import EMAIL
from database import Base
import re
from sqlalchemy.dialects.postgresql import UUID

class EmailVerificationCode(Base):
    '''Email Verification model'''
    __tablename__ = 'email_verication_codes'
    #__table_args__ = ({'schema':'public'},)

    email = Column(String(255), unique=True, primary_key=True)
    
    @validates('email')
    def validate_email(self, key, value):
        assert re.search(EMAIL, value), 'invalid email format'
        return value

# class RevokedToken(Base):
#     __tablename__ = 'revoked_tokens'
#     #__table_args__ = ({'schema':'public'},)
#     id = Column(Integer,primary_key=True,index=True)
#     jti = Column(String(255))

class TokenTable(Base):
    __tablename__ = "tokens"
    id = Column(Integer)
    access_toke = Column(String(450), primary_key=True)
    refresh_toke = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

@event.listens_for(EmailVerificationCode, 'before_insert')
def delete_existing_value(mapper, connection, target):
    with connection.begin():
        connection.execute(
            EmailVerificationCode.__table__.delete().where(EmailVerificationCode.__table__.c.email == target.email)
        )