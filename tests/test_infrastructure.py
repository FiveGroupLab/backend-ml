"""
Unit tests for infrastructure layer.
"""

import pytest
import pandas as pd
from unittest.mock import Mock, patch, MagicMock
from app.infrastructure.ml_models import JoblibModelRepository
from app.infrastructure.openai_service import OpenAIRecommendationService


class TestJoblibModelRepository:
    """Test cases for JoblibModelRepository."""
    
    @patch('app.infrastructure.ml_models.joblib.load')
    @patch('app.infrastructure.ml_models.Path.exists')
    def test_load_models(self, mock_exists, mock_joblib_load):
        """Test model loading."""
        mock_exists.return_value = True
        mock_model = Mock()
        mock_joblib_load.return_value = mock_model
        
        repo = JoblibModelRepository()
        
        assert len(repo.get_available_models()) == 3
        assert 'LOG' in repo.get_available_models()
        assert 'RF' in repo.get_available_models()
        assert 'XGB' in repo.get_available_models()
    
    @patch('app.infrastructure.ml_models.joblib.load')
    @patch('app.infrastructure.ml_models.Path.exists')
    def test_predict(self, mock_exists, mock_joblib_load):
        """Test prediction functionality."""
        mock_exists.return_value = True
        mock_model = Mock()
        mock_model.predict.return_value = [1]
        mock_joblib_load.return_value = mock_model
        
        repo = JoblibModelRepository()
        data = pd.DataFrame([[25.0, 150.0, 120.0, 70.0, 30]])
        
        result = repo.predict('LOG', data)
        assert result == 1
        mock_model.predict.assert_called_once_with(data)
    
    @patch('app.infrastructure.ml_models.joblib.load')
    @patch('app.infrastructure.ml_models.Path.exists')
    def test_predict_invalid_model(self, mock_exists, mock_joblib_load):
        """Test prediction with invalid model name."""
        mock_exists.return_value = True
        mock_joblib_load.return_value = Mock()
        
        repo = JoblibModelRepository()
        data = pd.DataFrame([[25.0, 150.0, 120.0, 70.0, 30]])
        
        with pytest.raises(ValueError, match="Model INVALID not found"):
            repo.predict('INVALID', data)


class TestOpenAIRecommendationService:
    """Test cases for OpenAIRecommendationService."""
    
    @patch('app.infrastructure.openai_service.OpenAI')
    @patch('app.infrastructure.openai_service.os.getenv')
    def test_init(self, mock_getenv, mock_openai):
        """Test service initialization."""
        mock_getenv.return_value = "test-api-key"
        service = OpenAIRecommendationService()
        mock_openai.assert_called_once_with(api_key="test-api-key")
    
    @patch('app.infrastructure.openai_service.asyncio.to_thread')
    @patch('app.infrastructure.openai_service.OpenAI')
    @patch('app.infrastructure.openai_service.os.getenv')
    @pytest.mark.asyncio
    async def test_generate_recommendation(self, mock_getenv, mock_openai, mock_to_thread):
        """Test recommendation generation."""
        mock_getenv.return_value = "test-api-key"

        # Create proper mock structure for OpenAI response
        mock_message = Mock()
        mock_message.content = "Recomendación médica"
        mock_choice = Mock()
        mock_choice.message = mock_message
        mock_response = Mock()
        mock_response.choices = [mock_choice]

        mock_to_thread.return_value = mock_response

        service = OpenAIRecommendationService()
        result = await service.generate_recommendation("Sí")

        assert result == "Recomendación médica"
        mock_to_thread.assert_called_once()

    @patch('app.infrastructure.ml_models.joblib.load')
    @patch('app.infrastructure.ml_models.Path.exists')
    def test_model_file_not_exists(self, mock_exists, mock_joblib_load):
        """Test behavior when model files don't exist."""
        mock_exists.return_value = False

        repo = JoblibModelRepository()
        assert len(repo.get_available_models()) == 0
        mock_joblib_load.assert_not_called()

    @patch('app.infrastructure.openai_service.OpenAI')
    @patch('app.infrastructure.openai_service.os.getenv')
    def test_openai_service_no_api_key(self, mock_getenv, mock_openai):
        """Test OpenAI service initialization without API key."""
        mock_getenv.return_value = None
        mock_client = Mock()
        mock_openai.return_value = mock_client

        service = OpenAIRecommendationService()
        assert service.client is not None
        mock_openai.assert_called_once_with(api_key=None)