# API Documentation

## Overview

The Hypertension Prediction API provides endpoints for assessing hypertension risk using machine learning models.

## Base URL

```
http://127.0.0.1:8000
```

## Endpoints

### POST /predict

Predicts hypertension risk for a patient using multiple ML models.

#### Request Body

```json
{
  "peso": 70.0,
  "estatura": 1.75,
  "actividad_total": 150.0,
  "tension_arterial": 120.0,
  "edad": 30
}
```

**Parameters:**
- `peso` (float): Patient weight in kg
- `estatura` (float): Patient height in meters
- `actividad_total` (float): Total physical activity score
- `tension_arterial` (float): Blood pressure measurement
- `edad` (int): Patient age in years

#### Response

```json
{
  "riesgo_hipertension": [
    {
      "modelo": "LOG",
      "prediccion": "No",
      "respuesta": "Mantener hábitos saludables..."
    },
    {
      "modelo": "RF",
      "prediccion": "No", 
      "respuesta": "Continuar con ejercicio regular..."
    },
    {
      "modelo": "XGB",
      "prediccion": "Sí",
      "respuesta": "Se recomienda consultar con un médico..."
    }
  ]
}
```

**Response Fields:**
- `modelo` (string): Model name (LOG, RF, XGB)
- `prediccion` (string): Prediction result ("Sí" or "No")
- `respuesta` (string): AI-generated medical recommendation

#### Status Codes

- `200 OK`: Successful prediction
- `422 Unprocessable Entity`: Invalid input data
- `500 Internal Server Error`: Server error

## Interactive Documentation

Visit `/docs` for Swagger UI documentation or `/redoc` for ReDoc documentation when the server is running.

## Example Usage

### cURL

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "peso": 70.0,
    "estatura": 1.75,
    "actividad_total": 150.0,
    "tension_arterial": 120.0,
    "edad": 30
  }'
```

### Python

```python
import requests

data = {
    "peso": 70.0,
    "estatura": 1.75,
    "actividad_total": 150.0,
    "tension_arterial": 120.0,
    "edad": 30
}

response = requests.post("http://127.0.0.1:8000/predict", json=data)
result = response.json()
print(result)
```