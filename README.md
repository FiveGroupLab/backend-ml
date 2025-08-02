# Prediction Backend

## Description

This is a backend project developed with FastAPI that provides an API to support prediction services for hypertension risk. The backend receives user input, processes it using a pre-trained machine learning model, and returns prediction results.  
**Note:** This repository contains only the backend logic; the frontend interface is managed separately.

## Main Features

- RESTful API to handle prediction requests
- CORS-enabled for frontend integration
- Model loading from a serialized `.pkl` file
- Integration-ready endpoints
- Auto-generated Swagger documentation

## Technologies Used

- FastAPI (0.115.12)
- Uvicorn (ASGI server)
- Scikit-learn
- Python 3.10+
- Pydantic

## Prerequisites

- Python 3.10 or higher
- Pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FiveGroupLab/backend-ml.git
   cd backend-ml
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/macOS
   venv\Scripts\activate        # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Open your browser and go to http://127.0.0.1:8000/docs

## Usage

- Send a POST request to /predict with the required data in JSON format.
- Receive prediction results in the response body.
- Use /docs to explore and test the API via Swagger UI.

## Architecture

This project follows a layered architecture pattern:

- **Domain Layer**: Core business logic and entities
- **Application Layer**: Use cases and workflows
- **Infrastructure Layer**: External dependencies (ML models, OpenAI)
- **Presentation Layer**: API endpoints and serialization

For detailed architecture documentation, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Testing

Run the comprehensive test suite:

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx
pip install pytest-cov


# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/
```

For detailed testing documentation, see [docs/TESTING.md](docs/TESTING.md).

## Project Structure

```
backend-ml/
├── app/
│   ├── domain/                    # Business logic and entities
│   │   ├── entities.py
│   │   └── repositories.py
│   ├── application/               # Use cases and workflows
│   │   └── use_cases.py
│   ├── infrastructure/            # External dependencies
│   │   ├── ml_models.py
│   │   └── openai_service.py
│   ├── presentation/              # API layer
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── ml_models/                 # Trained ML models
│   │   ├── modelo_hipertension_LOG.pkl
│   │   ├── modelo_hipertension_RF.pkl
│   │   └── modelo_hipertension_XGB.pkl
│   └── main.py
├── tests/                         # Unit tests
│   ├── test_domain.py
│   ├── test_application.py
│   ├── test_infrastructure.py
│   └── test_presentation.py
├── docs/                          # Documentation
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── TESTING.md
├── pytest.ini
├── requirements.txt
├── LICENSE
└── README.md
```

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you would like to change.

## License

[MIT](./LICENSE)

## Team Members

**Group Name:** GRUPO 5

- Berrio Huamani, Miguel Berrio (25207049)
- De La Cruz Hernandez, José Alexander (25207055)
- Ochoa Palacios, Eddy Leonardo (25207064)
- Ponte Paz, Junior Alexander (25207067)
- Yauri Martinez, Luis David (25207075)

## Contact

For questions or suggestions, please contact any of the team members.
