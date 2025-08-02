from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.presentation.routes import router

app = FastAPI(
    title="API de Predicción de Hipertensión",
    version="1.0.0",
    description="API for hypertension risk prediction using machine learning models"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
