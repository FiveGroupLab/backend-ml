from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

ruta_modelo = Path(__file__).parent / 'app' / 'ml_models' / 'modelo_hipertension.pkl'
modelo = joblib.load(ruta_modelo)

class EntradaModelo(BaseModel):
    masa_corporal: float
    actividad_total: float
    tension_arterial: float
    peso_promedio: float
    imc_binario: int
    edad: int

@app.post("/predict")
async def predecir(datos: EntradaModelo):
    entrada = pd.DataFrame(
        [[
            datos.masa_corporal,
            datos.actividad_total,
            datos.tension_arterial,
            datos.peso_promedio,
            datos.imc_binario,
            datos.edad
        ]],
        columns=["masa_corporal", "actividad_total", "tension_arterial", "peso_promedio", "imc_binario", "edad"]
    )

    pred = modelo.predict(entrada)[0]
    riesgo = "Sí" if pred == 1 else "No"

    return {"riesgo_hipertension": riesgo}

# @app.get("/")
# async def root():
#     print(ruta_modelo)
#     # print(ruta_modelo.exists())

#     # Crear DataFrame con las columnas y el orden esperado
#     # nueva_muestra_df = pd.DataFrame(
#     #     [[24, 240, 104, 96.75, 0, 65]],
#     #     columns=["masa_corporal", "actividad_total", "tension_arterial", "peso_promedio", "imc_binario", "edad"]
#     # )

#     # Predecir usando el modelo
#     # pred = modelo.predict(nueva_muestra_df)[0]

#     # respuesta = "Sí" if pred == 1 else "No"
#     # return {"riesgo_hipertension": respuesta}
#     return ruta_modelo

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
