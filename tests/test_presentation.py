"""
Unit tests for presentation layer.
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, AsyncMock, patch
from app.main import app
from app.domain.entities import PatientData, PredictionResult, HypertensionAssessment


class TestAPIRoutes:
    """Test cases for API routes."""
    
    @pytest.fixture
    def client(self):
        """Create test client."""
        return TestClient(app)
    
    @pytest.fixture
    def sample_request(self):
        """Sample API request data."""
        return {
            "peso": 70.0,
            "estatura": 1.75,
            "actividad_total": 150.0,
            "tension_arterial": 120.0,
            "edad": 30
        }
    
    @pytest.fixture
    def mock_assessment(self):
        """Mock hypertension assessment."""
        patient_data = PatientData(
            peso=70.0,
            estatura=1.75,
            actividad_total=150.0,
            tension_arterial=120.0,
            edad=30
        )
        predictions = [
            PredictionResult(
                modelo="LOG",
                prediccion="No",
                respuesta="Mantener hábitos saludables"
            ),
            PredictionResult(
                modelo="RF",
                prediccion="No",
                respuesta="Continuar con ejercicio"
            ),
            PredictionResult(
                modelo="XGB",
                prediccion="Sí",
                respuesta="Consultar médico"
            )
        ]
        return HypertensionAssessment(patient_data=patient_data, predictions=predictions)

    def test_predict_endpoint_validation_error(self, client):
        """Test prediction endpoint with invalid data."""
        invalid_request = {
            "peso": "invalid",  # Should be float
            "estatura": 1.75,
            "actividad_total": 150.0,
            "tension_arterial": 120.0,
            "edad": 30
        }

        response = client.post("/predict", json=invalid_request)
        assert response.status_code == 422

    def test_predict_endpoint_missing_fields(self, client):
        """Test prediction endpoint with missing required fields."""
        incomplete_request = {
            "peso": 70.0,
            "estatura": 1.75
            # Missing other required fields
        }

        response = client.post("/predict", json=incomplete_request)
        assert response.status_code == 422

        # Verify error details
        error_data = response.json()
        assert "detail" in error_data


class TestSchemas:
    """Test cases for API schemas."""

    def test_patient_data_request_valid(self):
        """Test valid patient data request schema."""
        from app.presentation.schemas import PatientDataRequest

        data = {
            "peso": 70.0,
            "estatura": 1.75,
            "actividad_total": 150.0,
            "tension_arterial": 120.0,
            "edad": 30
        }

        request = PatientDataRequest(**data)
        assert request.peso == 70.0
        assert request.estatura == 1.75
        assert request.actividad_total == 150.0
        assert request.tension_arterial == 120.0
        assert request.edad == 30

    def test_prediction_response_schema(self):
        """Test prediction response schema."""
        from app.presentation.schemas import PredictionResponse

        response = PredictionResponse(
            modelo="LOG",
            prediccion="Sí",
            respuesta="Recomendación médica"
        )

        assert response.modelo == "LOG"
        assert response.prediccion == "Sí"
        assert response.respuesta == "Recomendación médica"

    @patch('app.infrastructure.openai_service.OpenAI')
    @patch('app.infrastructure.openai_service.os.getenv')
    @patch('app.infrastructure.ml_models.joblib.load')
    @patch('app.infrastructure.ml_models.Path.exists')
    def test_dependency_injection(self, mock_exists, mock_joblib_load, mock_getenv, mock_openai):
        """Test dependency injection in routes."""
        from app.presentation.routes import get_prediction_use_case

        mock_getenv.return_value = "test-api-key"
        mock_openai.return_value = Mock()
        mock_exists.return_value = True
        mock_joblib_load.return_value = Mock()

        use_case = get_prediction_use_case()
        assert use_case is not None
        assert hasattr(use_case, 'predict_hypertension_risk')