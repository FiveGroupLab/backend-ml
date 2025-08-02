"""
Unit tests for application layer.
"""

import pytest
from unittest.mock import Mock, AsyncMock
import pandas as pd
from app.application.use_cases import HypertensionPredictionUseCase
from app.domain.entities import PatientData, PredictionResult


class TestHypertensionPredictionUseCase:
    """Test cases for HypertensionPredictionUseCase."""
    
    @pytest.fixture
    def mock_model_repo(self):
        """Mock model repository."""
        repo = Mock()
        repo.get_available_models.return_value = ['LOG', 'RF', 'XGB']
        repo.predict.return_value = 1
        return repo
    
    @pytest.fixture
    def mock_recommendation_service(self):
        """Mock recommendation service."""
        service = AsyncMock()
        service.generate_recommendation.return_value = "Recomendación médica"
        return service
    
    @pytest.fixture
    def use_case(self, mock_model_repo, mock_recommendation_service):
        """Create use case with mocked dependencies."""
        return HypertensionPredictionUseCase(mock_model_repo, mock_recommendation_service)
    
    @pytest.fixture
    def patient_data(self):
        """Sample patient data."""
        return PatientData(
            peso=70.0,
            estatura=1.75,
            actividad_total=150.0,
            tension_arterial=120.0,
            edad=30
        )
    
    @pytest.mark.asyncio
    async def test_predict_hypertension_risk(self, use_case, patient_data, mock_model_repo, mock_recommendation_service):
        """Test hypertension risk prediction."""
        assessment = await use_case.predict_hypertension_risk(patient_data)

        assert assessment.patient_data == patient_data
        assert len(assessment.predictions) == 3

        # Verify model repository calls
        assert mock_model_repo.get_available_models.called
        assert mock_model_repo.predict.call_count == 3

        # Verify recommendation service calls
        assert mock_recommendation_service.generate_recommendation.call_count == 3

    @pytest.mark.asyncio
    async def test_generate_prediction(self, use_case, mock_model_repo, mock_recommendation_service):
        """Test individual prediction generation."""
        input_data = pd.DataFrame([[25.0, 150.0, 120.0, 70.0, 30]])

        result = await use_case._generate_prediction('LOG', input_data)

        assert isinstance(result, PredictionResult)
        assert result.modelo == 'LOG'
        assert result.prediccion == 'Sí'
        assert result.respuesta == "Recomendación médica"

        mock_model_repo.predict.assert_called_once_with('LOG', input_data)
        mock_recommendation_service.generate_recommendation.assert_called_once_with('Sí')

    @pytest.mark.asyncio
    async def test_prediction_no_risk(self, use_case, mock_model_repo, mock_recommendation_service):
        """Test prediction when no risk is detected."""
        mock_model_repo.predict.return_value = 0
        input_data = pd.DataFrame([[25.0, 150.0, 120.0, 70.0, 30]])

        result = await use_case._generate_prediction('LOG', input_data)

        assert result.prediccion == 'No'
        mock_recommendation_service.generate_recommendation.assert_called_once_with('No')

    @pytest.mark.asyncio
    async def test_data_preparation(self, use_case, patient_data, mock_model_repo, mock_recommendation_service):
        """Test input data preparation for models."""
        await use_case.predict_hypertension_risk(patient_data)

        # Verify model was called with correct data structure
        call_args = mock_model_repo.predict.call_args_list[0][0]
        input_data = call_args[1]

        assert list(input_data.columns) == ["IMC_calculado", "actividad_total", "tension_arterial", "peso_promedio", "edad"]
        assert input_data.iloc[0]['IMC_calculado'] == patient_data.calculate_imc()