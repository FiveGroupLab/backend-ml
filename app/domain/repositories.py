"""
Repository interfaces for the domain layer.

This module defines the contracts that infrastructure components
must implement to provide data access and external services.
"""

from abc import ABC, abstractmethod
from typing import List
import pandas as pd
from .entities import PredictionResult


class ModelRepository(ABC):
    """Interface for ML model access."""
    
    @abstractmethod
    def predict(self, model_name: str, data: pd.DataFrame) -> int:
        """Make prediction using specified model."""
        pass
    
    @abstractmethod
    def get_available_models(self) -> List[str]:
        """Get list of available model names."""
        pass


class RecommendationService(ABC):
    """Interface for generating recommendations."""
    
    @abstractmethod
    async def generate_recommendation(self, prediction: str) -> str:
        """Generate recommendation based on prediction."""
        pass