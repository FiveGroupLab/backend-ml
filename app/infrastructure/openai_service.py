"""
OpenAI service implementation.

This module provides the concrete implementation for generating
medical recommendations using OpenAI's API.
"""

import os
import asyncio
from openai import OpenAI
from dotenv import load_dotenv
from ..domain.repositories import RecommendationService

load_dotenv()


class OpenAIRecommendationService(RecommendationService):
    """OpenAI-based recommendation service."""
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    async def generate_recommendation(self, prediction: str) -> str:
        """Generate recommendation based on prediction."""
        prompt = (
            f"En base a la siguiente predicción sobre el riesgo de hipertensión: '{prediction}', "
            "¿qué me podrías recomendar? Por favor responde en un párrafo breve y completo."
        )
        
        response = await asyncio.to_thread(
            self.client.chat.completions.create,
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un asistente médico experto en hipertensión."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        
        return response.choices[0].message.content.strip()