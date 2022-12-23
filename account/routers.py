from fastapi import APIRouter
from account.models import Account

routers = APIRouter()

@routers.get('/')
async def helloworld():
    return {'msg': 'Hello World'}

@routers.get('/author')
async def author():
    account = Account(
        username="dev.diego.afc@gmail.com",
        password="mysuperpass",
        name="Diego Feitosa"
    )
    return account
