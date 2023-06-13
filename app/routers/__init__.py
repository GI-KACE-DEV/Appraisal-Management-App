from routers.users import * 

from routers.staffs import *

from database import Base, engine

__all__ = [
    'users',
    'staffs',
    'user_type',
    'appraisal_forms'
]
#tables=[table for table in Base.metadata.sorted_tables if table.schema=='public' or table.schema=='global']
Base.metadata.create_all(bind=engine) 