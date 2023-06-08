from typing import Optional
from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    username: str 
    email: EmailStr 
    password: str 

class ShowUser(BaseModel):
    username: str 
    email : EmailStr 
    is_active : bool

    class Config():
        orm_model = True 
    



class Login(BaseModel):
    username: str
    password: str 

    class Config():
        orm_mode = True





class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None 