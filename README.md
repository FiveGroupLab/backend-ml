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

   git clone https://github.com/FiveGroupLab/backend-ml.git
   cd backend-ml

2. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate     # Linux/macOS
   venv\Scripts\activate        # Windows

3. Install dependencies:

   pip install -r requirements.txt

4. Run the development server:

   uvicorn app.main:app --reload

5. Open your browser and go to http://127.0.0.1:8000/docs

## Usage

- Send a POST request to /predict with the required data in JSON format.
- Receive prediction results in the response body.
- Use /docs to explore and test the API via Swagger UI.

## Project Structure

```
backend-ml/
├── app/
│ ├── api/
│ │ └── routes.py
│ ├── ml_models/
│ │ ├── modelo_hipertension.pk
│ │ ├── init.py
│ │ ├── main.py
│ │ ├── models.py
│ │ ├── routes.py
│ │ └── services.py
│ └── pycache/
├── test/
│ └── test_main.htt
├── LICENSE
├── README.md
└── requirements.txt
```

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you would like to change.

## License

MIT

## Team Members

**Group Name:** GRUPO 5

- Berrio Huamani, Miguel Berrio (25207049)
- De La Cruz Hernandez, José Alexander (25207055)
- Ochoa Palacios, Eddy Leonardo (25207064)
- Ponte Paz, Junior Alexander (25207067)
- Yauri Martinez, Luis David (25207075)

## Contact

For questions or suggestions, please contact any of the team members.
