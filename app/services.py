import pandas as pd
from pathlib import Path
import joblib

ruta_modelo = Path(__file__).parent / 'ml_models' / 'modelo_hipertension.pkl'
modelo = joblib.load(ruta_modelo)

def predecir_riesgo(datos) -> str:
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

    pred = modelo.predict(entrada)[0]
    return "Sí" if pred == 1 else "No"
