"""
Domain entities for hypertension prediction system.

This module contains the core business entities that represent
the fundamental concepts in the hypertension prediction domain.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class PatientData:
    """Patient data for hypertension risk assessment."""
    peso: float
    estatura: float
    actividad_total: float
    tension_arterial: float
    edad: int

    def calculate_imc(self) -> float:
        """Calculate BMI from weight and height."""
        return self.peso / (self.estatura ** 2)


@dataclass
class PredictionResult:
    """Result of a hypertension prediction."""
    modelo: str
    prediccion: str
    respuesta: str


@dataclass
class HypertensionAssessment:
    """Complete hypertension risk assessment."""
    patient_data: PatientData
    predictions: List[PredictionResult]