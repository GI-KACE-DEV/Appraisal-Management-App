from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean(),default=True)
    is_superuser = Column(Boolean(),default=False)
    satff = relationship("Staff", back_populates="user")

## 
