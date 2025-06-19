# Prediction Backend

## Description

This is a backend API developed with FastAPI that provides prediction services for hypertension risk. It is designed to be consumed by a separate frontend interface. The API exposes endpoints that receive user data and return prediction results based on a trained machine learning model.

> **Note:** This repository contains only the backend logic; the frontend interface is managed separately.

## Main Features

- REST API built with FastAPI
- Machine learning model served using `scikit-learn`
- Pretrained `.pkl` model loaded at runtime
- CORS enabled to allow frontend integration

## Technologies Used

- FastAPI (0.115.12)
- Uvicorn (ASGI server)
- Scikit-learn
- Python 3.10+
- Pydantic

## Endpoints

- `POST /predict`: Receives user input and returns a prediction
- `GET /docs`: Swagger UI for interactive API documentation

## Prerequisites

- Python 3.10 or higher
- Pip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/FiveGroupLab/backend-ml.git
   cd backend-ml
