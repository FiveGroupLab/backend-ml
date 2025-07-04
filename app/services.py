from pathlib import Path

import joblib
import pandas as pd
from openai import OpenAI
from pydantic import BaseModel

ruta_modelo_1 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension.pkl'
modelo_1 = joblib.load(ruta_modelo_1)
ruta_modelo_2 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension.pkl'
modelo_2 = joblib.load(ruta_modelo_2)
ruta_modelo_3 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension.pkl'
modelo_3 = joblib.load(ruta_modelo_3)


class Response(BaseModel):
    prediccion: str
    respuesta: str


client = OpenAI(
    api_key="Agregar_token"
)


def predecir_riesgo(datos) -> list[Response]:
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

    modelos = [modelo_1, modelo_2, modelo_3]
    resultados = []

    for modelo in modelos:
        prediccion = modelo.predict(entrada)[0]
        prediccion_str = "Sí" if prediccion == 1 else "No"

        # Formulamos la consulta personalizada al modelo GPT
        prompt = f"En base a la siguiente predicción sobre el riesgo de hipertensión: '{prediccion_str}', ¿qué me podrías recomendar? Por favor responde en un párrafo breve y completo."

        response = client.chat.completions.create(  # Usamos chat.completions que es la API correcta
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un asistente médico experto en hipertensión."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        respuesta_texto = response.choices[0].message.content.strip()

        # Guardamos tanto la predicción como la respuesta
        resultados.append(Response(prediccion=prediccion_str, respuesta=respuesta_texto))

    return resultados
