"""
API schemas for the presentation layer.

This module defines the data transfer objects (DTOs) used
for API request and response serialization.
"""

from pydantic import BaseModel
from typing import List


class PatientDataRequest(BaseModel):
    """Request schema for patient data."""
    peso: float
    estatura: float
    actividad_total: float
    tension_arterial: float
    edad: int


class PredictionResponse(BaseModel):
    """Response schema for individual prediction."""
    modelo: str
    prediccion: str
    respuesta: str


class HypertensionRiskResponse(BaseModel):
    """Response schema for hypertension risk assessment."""
    riesgo_hipertension: List[PredictionResponse]