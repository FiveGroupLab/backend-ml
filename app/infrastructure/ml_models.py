"""
ML model infrastructure implementation.

This module provides concrete implementations for loading and using
machine learning models for hypertension prediction.
"""

from pathlib import Path
from typing import List, Dict, Any
import joblib
import pandas as pd
from ..domain.repositories import ModelRepository


class JoblibModelRepository(ModelRepository):
    """Repository for joblib-serialized ML models."""
    
    def __init__(self):
        self._models: Dict[str, Any] = {}
        self._load_models()
    
    def _load_models(self) -> None:
        """Load all available models from disk."""
        model_path = Path(__file__).parent.parent / 'ml_models'
        model_files = {
            'LOG': 'modelo_hipertension_LOG.pkl',
            'RF': 'modelo_hipertension_RF.pkl',
            'XGB': 'modelo_hipertension_XGB.pkl'
        }
        
        for name, filename in model_files.items():
            file_path = model_path / filename
            if file_path.exists():
                self._models[name] = joblib.load(file_path)
    
    def predict(self, model_name: str, data: pd.DataFrame) -> int:
        """Make prediction using specified model."""
        if model_name not in self._models:
            raise ValueError(f"Model {model_name} not found")
        return self._models[model_name].predict(data)[0]
    
    def get_available_models(self) -> List[str]:
        """Get list of available model names."""
        return list(self._models.keys())