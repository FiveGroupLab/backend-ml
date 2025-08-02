"""
Use cases for hypertension prediction system.

This module contains the application-specific business logic
that orchestrates domain entities and repository operations.
"""

import asyncio
from typing import List
import pandas as pd
from ..domain.entities import PatientData, PredictionResult, HypertensionAssessment
from ..domain.repositories import ModelRepository, RecommendationService


class HypertensionPredictionUseCase:
    """Use case for predicting hypertension risk."""
    
    def __init__(self, model_repo: ModelRepository, recommendation_service: RecommendationService):
        self.model_repo = model_repo
        self.recommendation_service = recommendation_service
    
    async def predict_hypertension_risk(self, patient_data: PatientData) -> HypertensionAssessment:
        """Predict hypertension risk for a patient."""
        # Prepare input data
        imc = patient_data.calculate_imc()
        input_data = pd.DataFrame(
            [[
                imc,
                patient_data.actividad_total,
                patient_data.tension_arterial,
                patient_data.peso,
                patient_data.edad
            ]],
            columns=["IMC_calculado", "actividad_total", "tension_arterial", "peso_promedio", "edad"]
        )
        
        # Get predictions from all models
        models = self.model_repo.get_available_models()
        tasks = [self._generate_prediction(model, input_data) for model in models]
        predictions = await asyncio.gather(*tasks)
        
        return HypertensionAssessment(
            patient_data=patient_data,
            predictions=predictions
        )
    
    async def _generate_prediction(self, model_name: str, input_data: pd.DataFrame) -> PredictionResult:
        """Generate prediction and recommendation for a single model."""
        prediction = self.model_repo.predict(model_name, input_data)
        prediction_str = "Sí" if prediction == 1 else "No"
        recommendation = await self.recommendation_service.generate_recommendation(prediction_str)
        
        return PredictionResult(
            modelo=model_name,
            prediccion=prediction_str,
            respuesta=recommendation
        )