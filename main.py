from fastapi import FastAPI
from account.routers import routers

app = FastAPI()
app.include_router(routers, prefix='/account', tags=['accounts', 'contas'])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0", port=8000, log_level='info', reload=True)
