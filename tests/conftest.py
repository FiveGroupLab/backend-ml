"""
Test configuration and fixtures.
"""

import os
import pytest
from unittest.mock import patch


@pytest.fixture(autouse=True)
def mock_openai_env():
    """Mock OpenAI environment variables for all tests."""
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test-api-key"}):
        yield


@pytest.fixture(autouse=True)
def mock_openai_client():
    """Mock OpenAI client for all tests."""
    with patch('app.infrastructure.openai_service.OpenAI') as mock_openai:
        mock_client = mock_openai.return_value
        yield mock_client