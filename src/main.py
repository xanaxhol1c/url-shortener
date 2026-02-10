from fastapi import FastAPI
from src.routes.urls import router as urls_router

app = FastAPI()

app.include_router(urls_router)