from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from services.ai_service import analyze_document, AnalysisError

app = FastAPI(title='AI Insights Service')

class AnalyzeRequest(BaseModel):
    document_id: int = Field(..., gt=0)
    title: str = Field(..., min_length=5)
    content: str = Field(..., min_length=50)

class AnalyzeResponse(BaseModel):
    document_id: int
    summary: str
    score: float
    tags: list[str]
    warnings: list[str] = []

@app.post('/analyze', response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    try:
        return await analyze_document(request)
    except AnalysisError as error:
        raise HTTPException(status_code=503, detail=error.message)
    except Exception as error:
        raise HTTPException(status_code=500, detail='AI service encountered an unexpected error')

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={'code': 'AI_SERVICE_ERROR', 'message': exc.detail})
