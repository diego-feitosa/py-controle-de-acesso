from fastapi import APIRouter

from account.routers import routers as account_routers

api_routers = APIRouter()

api_routers.include_router(account_routers, prefix="/accounts", tags=['accounts'])
