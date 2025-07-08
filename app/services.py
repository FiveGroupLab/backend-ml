from pathlib import Path

import joblib
import pandas as pd
from openai import OpenAI
from pydantic import BaseModel
import os

load_dotenv()

ruta_modelo_1 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension_LOG.pkl'
modelo_1 = joblib.load(ruta_modelo_1)
ruta_modelo_2 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension_RF.pkl'
modelo_2 = joblib.load(ruta_modelo_2)
ruta_modelo_3 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension_XGB.pkl'
modelo_3 = joblib.load(ruta_modelo_3)

class Response(BaseModel):
    modelo: str
    prediccion: str
    respuesta: str

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def predecir_riesgo(datos) -> list[Response]:
    imc = datos.peso / (datos.estatura ** 2)

    entrada = pd.DataFrame(
        [[
            imc,
            datos.actividad_total,
            datos.tension_arterial,
            datos.peso,
            datos.edad            
        ]],
        columns=["IMC_calculado", "actividad_total", "tension_arterial","peso_promedio", "edad"]
    )

    modelos = [
        ("LOG", modelo_1),
        ("RF", modelo_2),
        ("XGB", modelo_3)
    ]

    resultados = []

    for nombre_modelo, modelo in modelos:
        prediccion = modelo.predict(entrada)[0]
        prediccion_str = "Sí" if prediccion == 1 else "No"

        prompt = f"En base a la siguiente predicción sobre el riesgo de hipertensión: '{prediccion_str}', ¿qué me podrías recomendar? Por favor responde en un párrafo breve y completo."

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un asistente médico experto en hipertensión."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        respuesta_texto = response.choices[0].message.content.strip()

        resultados.append(Response(
            modelo=nombre_modelo,
            prediccion=prediccion_str,
            respuesta=respuesta_texto
        ))

    return resultados
