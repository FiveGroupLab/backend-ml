"""
API routes for hypertension prediction.

This module defines the FastAPI routes and handles HTTP requests
for the hypertension prediction service.
"""

from fastapi import APIRouter, Depends
from .schemas import PatientDataRequest, HypertensionRiskResponse, PredictionResponse
from ..domain.entities import PatientData
from ..application.use_cases import HypertensionPredictionUseCase
from ..infrastructure.ml_models import JoblibModelRepository
from ..infrastructure.openai_service import OpenAIRecommendationService

router = APIRouter()

# Dependency injection
def get_prediction_use_case() -> HypertensionPredictionUseCase:
    """Create and return prediction use case with dependencies."""
    model_repo = JoblibModelRepository()
    recommendation_service = OpenAIRecommendationService()
    return HypertensionPredictionUseCase(model_repo, recommendation_service)


@router.post("/predict", response_model=HypertensionRiskResponse)
async def predict_hypertension_risk(
    request: PatientDataRequest,
    use_case: HypertensionPredictionUseCase = Depends(get_prediction_use_case)
) -> HypertensionRiskResponse:
    """Predict hypertension risk for a patient."""
    patient_data = PatientData(
        peso=request.peso,
        estatura=request.estatura,
        actividad_total=request.actividad_total,
        tension_arterial=request.tension_arterial,
        edad=request.edad
    )
    
    assessment = await use_case.predict_hypertension_risk(patient_data)
    
    predictions = [
        PredictionResponse(
            modelo=pred.modelo,
            prediccion=pred.prediccion,
            respuesta=pred.respuesta
        )
        for pred in assessment.predictions
    ]
    
    return HypertensionRiskResponse(riesgo_hipertension=predictions)