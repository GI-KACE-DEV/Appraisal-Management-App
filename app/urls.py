from sys import prefix
from fastapi import APIRouter , WebSocket, Depends

from routers.users.account.main import user_acc_router
from routers.users.user_type.main import usertype_router
from routers.staffs.main import staff_router 
from routers.start_of_year.main import start_of_year_router 
from routers.mid_year_review.main import mid_year_review_router 
from routers.users.auth.main import auth_router
#from app.main import app
import config as cfg

api_router = APIRouter()



api_router.include_router(user_acc_router, tags=['User & Adminstrator Accounts'], prefix='/accounts')
api_router.include_router(staff_router, tags=['Staff'], prefix="/staff")
api_router.include_router(start_of_year_router, tags=['Start Of Year'], prefix="/startOfYear")
api_router.include_router(mid_year_review_router, tags=['Mid Year Review'], prefix="/midYearReview")
api_router.include_router(usertype_router, tags=['User Type'])
api_router.include_router(auth_router, prefix="/login", tags=["login"])