from fastapi import FastAPI
from app.routers.logs_router import router as logs_router

app = FastAPI(title="Log File Analysis API")

app.include_router(logs_router)


@app.get("/")
def root():
    return {"message": "Log API is running"}
