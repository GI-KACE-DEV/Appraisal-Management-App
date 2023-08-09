from routers.users import * 

from routers.staffs import *

from routers.appraisal_form import *

from routers.start_of_year.models import *

from routers.mid_year_review.models import *

from routers.users.user_type.models import *

from routers.end_of_year.models import *

from routers.performance_details.models import *

from routers.overall_performance.models import *

from routers.deadline.models import *


from database import Base, engine

# __all__ = [
#     'Base',
#     'account',
#     'auth',
#     'permission',
#     'role',
#     'staffs',
#     'user_type',
#     'appraisal_forms',
#     'content_type',
#     'deadline',
#     'end_of_year',
#     'mid_year_review',
# ]
#tables=[table for table in Base.metadata.sorted_tables if table.schema=='public' or table.schema=='global']
#tables=[table for table in Base.metadata.sorted_tables if table.schema=='public' or table.schema=='global']
#Base.metadata.create_all(bind=engine) 
Base.metadata.create_all(bind=engine)
