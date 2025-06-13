from fastapi import APIRouter
from .models import EntradaModelo
from .services import predecir_riesgo

router = APIRouter()

@router.post("/predict")
async def predict(datos: EntradaModelo):
    riesgo = predecir_riesgo(datos)
    return {"riesgo_hipertension": riesgo}
