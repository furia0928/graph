from fastapi import FastAPI
from src.api.endpoints import router as endpoints_router

app = FastAPI()
app.include_router(endpoints_router)
