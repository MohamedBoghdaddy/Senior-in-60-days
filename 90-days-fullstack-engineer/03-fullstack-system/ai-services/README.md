# AI Service

This FastAPI microservice provides safe, structured AI inference for the platform.

## Features

- request and response schema validation
- retry logic for transient failures
- fallback behavior when AI provider is unavailable
- structured logs for observability

## Endpoints

- `POST /analyze` - analyze a data payload and return a scored insight.

## Run locally

1. Install dependencies: `pip install fastapi uvicorn pydantic requests`
2. Start service: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
