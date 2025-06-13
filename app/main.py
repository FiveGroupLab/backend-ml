from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="API de Predicción de Hipertensión",
    version="1.0.0"
)

app.include_router(router)
