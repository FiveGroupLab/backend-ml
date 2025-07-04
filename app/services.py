from pathlib import Path

import joblib
import pandas as pd

ruta_modelo_1 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension.pkl'
modelo_1 = joblib.load(ruta_modelo_1)
ruta_modelo_2 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension.pkl'
modelo_2 = joblib.load(ruta_modelo_2)
ruta_modelo_3 = Path(__file__).parent / 'ml_models' / 'modelo_hipertension.pkl'
modelo_3 = joblib.load(ruta_modelo_3)


def predecir_riesgo(datos) -> list[str]:
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

    pred_1 = modelo_1.predict(entrada)[0]
    pred_2 = modelo_2.predict(entrada)[0]
    pred_3 = modelo_3.predict(entrada)[0]
    resultados = ["Sí" if pred == 1 else "No" for pred in [pred_1, pred_2, pred_3]]
    return resultados
