from fastapi import FastAPI
from core.routers import api_routers

app = FastAPI()

app.include_router(api_routers, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0", port=8000, log_level='info', reload=True)
