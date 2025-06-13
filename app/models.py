from pydantic import BaseModel

class EntradaModelo(BaseModel):
    peso: float
    estatura: float
    actividad_total: float
    tension_arterial: float
    edad: int
