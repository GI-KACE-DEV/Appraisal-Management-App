from routers.users import * 

from database import Base, engine

__all__ = [
    'users',
    'staff',
    'department_type',
    'user_type'
]
#tables=[table for table in Base.metadata.sorted_tables if table.schema=='public' or table.schema=='global']
Base.metadata.create_all(bind=engine) 