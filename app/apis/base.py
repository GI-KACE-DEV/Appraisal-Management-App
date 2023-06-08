from fastapi import APIRouter

import login_route, users_route



api_router = APIRouter()


api_router.include_router(users_route.router,prefix="",tags=["users"])
api_router.include_router(login_route.router,prefix="/login",tags=["login"])

