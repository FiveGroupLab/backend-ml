# Architecture Documentation

## Overview

This project follows a layered architecture pattern that separates concerns and promotes maintainability, testability, and scalability. The architecture is based on Clean Architecture principles.

## Layer Structure

### 1. Domain Layer (`app/domain/`)

The domain layer contains the core business logic and entities. It's independent of external frameworks and technologies.

**Components:**
- `entities.py`: Core business entities (PatientData, PredictionResult, HypertensionAssessment)
- `repositories.py`: Abstract interfaces for data access and external services

**Key Principles:**
- No dependencies on external frameworks
- Contains pure business logic
- Defines contracts through interfaces

### 2. Application Layer (`app/application/`)

The application layer orchestrates the business logic and coordinates between different components.

**Components:**
- `use_cases.py`: Application-specific business rules and workflows

**Key Principles:**
- Implements business workflows
- Coordinates domain entities and repository operations
- Independent of UI and infrastructure details

### 3. Infrastructure Layer (`app/infrastructure/`)

The infrastructure layer provides concrete implementations of the interfaces defined in the domain layer.

**Components:**
- `ml_models.py`: ML model loading and prediction implementation
- `openai_service.py`: OpenAI API integration for recommendations

**Key Principles:**
- Implements domain interfaces
- Handles external dependencies (databases, APIs, file systems)
- Can be easily replaced without affecting business logic

### 4. Presentation Layer (`app/presentation/`)

The presentation layer handles HTTP requests and responses, data serialization, and API documentation.

**Components:**
- `routes.py`: FastAPI route definitions and HTTP handling
- `schemas.py`: Pydantic models for request/response serialization

**Key Principles:**
- Handles HTTP protocol concerns
- Validates input data
- Serializes responses
- Provides API documentation

## Data Flow

1. **HTTP Request** → Presentation Layer receives and validates request
2. **Use Case Execution** → Application layer orchestrates business logic
3. **Domain Operations** → Core business rules are applied
4. **Infrastructure Calls** → External services (ML models, OpenAI) are invoked
5. **Response Formation** → Results are serialized and returned

## Benefits

- **Separation of Concerns**: Each layer has a single responsibility
- **Testability**: Easy to unit test each layer in isolation
- **Maintainability**: Changes in one layer don't affect others
- **Flexibility**: Easy to swap implementations (e.g., different ML frameworks)
- **Scalability**: Clear structure supports team collaboration