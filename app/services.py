from pathlib import Path
import joblib
import pandas as pd
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

ruta_modelo_1 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension_LOG.pkl'
modelo_1 = joblib.load(ruta_modelo_1)
ruta_modelo_2 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension_RF.pkl'
modelo_2 = joblib.load(ruta_modelo_2)
ruta_modelo_3 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension_XGB.pkl'
modelo_3 = joblib.load(ruta_modelo_3)

# Cliente OpenAI asincrónico
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Clase para la respuesta
class Response(BaseModel):
    modelo: str
    prediccion: str
    respuesta: str

# Función asincrónica para generar recomendación
async def generar_respuesta(nombre_modelo: str, modelo, entrada: pd.DataFrame) -> Response:
    prediccion = modelo.predict(entrada)[0]
    prediccion_str = "Sí" if prediccion == 1 else "No"

    prompt = f"En base a la siguiente predicción sobre el riesgo de hipertensión: '{prediccion_str}', ¿qué me podrías recomendar? Por favor responde en un párrafo breve y completo."

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Eres un asistente médico experto en hipertensión."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    print(response)

    respuesta_texto = response.choices[0].message.content.strip()

    print(respuesta_texto)

    return Response(
        modelo=nombre_modelo,
        prediccion=prediccion_str,
        respuesta=respuesta_texto
    )

# Función principal para predecir
async def predecir_riesgo(datos) -> list[Response]:
    imc = datos.peso / (datos.estatura ** 2)

    entrada = pd.DataFrame(
        [[
            imc,
            datos.actividad_total,
            datos.tension_arterial,
            datos.edad
        ]],
        columns=["IMC_calculado", "actividad_total", "tension_arterial", "edad"]
    )

    modelos = [
        ("LOG", modelo_1),
        ("RF", modelo_2),
        ("XGB", modelo_3)
    ]

    tareas = [generar_respuesta(nombre, modelo, entrada) for nombre, modelo in modelos]
    return await asyncio.gather(*tareas)