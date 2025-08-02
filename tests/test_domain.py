"""
Unit tests for domain layer.
"""

import pytest
from app.domain.entities import PatientData, PredictionResult, HypertensionAssessment


class TestPatientData:
    """Test cases for PatientData entity."""
    
    def test_calculate_imc(self):
        """Test BMI calculation."""
        patient = PatientData(
            peso=70.0,
            estatura=1.75,
            actividad_total=150.0,
            tension_arterial=120.0,
            edad=30
        )
        expected_imc = 70.0 / (1.75 ** 2)
        assert patient.calculate_imc() == pytest.approx(expected_imc, rel=1e-9)
    
    def test_patient_data_creation(self):
        """Test patient data creation."""
        patient = PatientData(
            peso=80.0,
            estatura=1.80,
            actividad_total=200.0,
            tension_arterial=130.0,
            edad=35
        )
        assert patient.peso == 80.0
        assert patient.estatura == 1.80
        assert patient.actividad_total == 200.0
        assert patient.tension_arterial == 130.0
        assert patient.edad == 35


class TestPredictionResult:
    """Test cases for PredictionResult entity."""
    
    def test_prediction_result_creation(self):
        """Test prediction result creation."""
        result = PredictionResult(
            modelo="LOG",
            prediccion="Sí",
            respuesta="Recomendación médica"
        )
        assert result.modelo == "LOG"
        assert result.prediccion == "Sí"
        assert result.respuesta == "Recomendación médica"


class TestHypertensionAssessment:
    """Test cases for HypertensionAssessment entity."""
    
    def test_assessment_creation(self):
        """Test assessment creation."""
        patient = PatientData(70.0, 1.75, 150.0, 120.0, 30)
        predictions = [
            PredictionResult("LOG", "No", "Mantener hábitos saludables"),
            PredictionResult("RF", "No", "Continuar con ejercicio")
        ]
        assessment = HypertensionAssessment(patient, predictions)
        
        assert assessment.patient_data == patient
        assert len(assessment.predictions) == 2
        assert assessment.predictions[0].modelo == "LOG"