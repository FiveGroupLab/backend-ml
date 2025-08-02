# Testing Documentation

## Overview

This project uses pytest for comprehensive unit testing across all architectural layers.

## Test Structure

```
tests/
├── __init__.py
├── test_domain.py          # Domain layer tests
├── test_infrastructure.py  # Infrastructure layer tests
├── test_application.py     # Application layer tests
└── test_presentation.py    # Presentation layer tests
```

## Running Tests

### Install Test Dependencies

```bash
pip install pytest pytest-asyncio httpx
```

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_domain.py
```

### Run with Coverage

```bash
pytest --cov=app tests/
```

### Run with Verbose Output

```bash
pytest -v
```

## Test Categories

### Domain Layer Tests (`test_domain.py`)

Tests core business entities and logic:
- PatientData BMI calculation
- Entity creation and validation
- Business rule enforcement

### Infrastructure Layer Tests (`test_infrastructure.py`)

Tests external service integrations:
- ML model loading and prediction
- OpenAI API integration
- Error handling for external dependencies

### Application Layer Tests (`test_application.py`)

Tests use case orchestration:
- End-to-end workflow testing
- Dependency coordination
- Business logic integration

### Presentation Layer Tests (`test_presentation.py`)

Tests API endpoints and serialization:
- HTTP request/response handling
- Input validation
- API contract compliance

## Test Patterns

### Mocking External Dependencies

```python
@patch('app.infrastructure.ml_models.joblib.load')
def test_model_loading(self, mock_joblib_load):
    mock_joblib_load.return_value = Mock()
    # Test implementation
```

### Async Testing

```python
async def test_async_function(self):
    result = await some_async_function()
    assert result is not None
```

### Fixture Usage

```python
@pytest.fixture
def patient_data():
    return PatientData(70.0, 1.75, 150.0, 120.0, 30)
```

## Best Practices

1. **Test Isolation**: Each test should be independent
2. **Mock External Dependencies**: Don't rely on external services in tests
3. **Clear Test Names**: Use descriptive test method names
4. **Arrange-Act-Assert**: Structure tests clearly
5. **Edge Cases**: Test boundary conditions and error scenarios

## Continuous Integration

Tests should be run automatically on:
- Pull requests
- Main branch commits
- Release builds

Example GitHub Actions workflow:

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.10
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: pytest
```