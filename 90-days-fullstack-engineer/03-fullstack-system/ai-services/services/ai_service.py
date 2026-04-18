import asyncio
from pydantic import BaseModel

class AnalysisError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class AnalyzeRequest(BaseModel):
    document_id: int
    title: str
    content: str

async def call_external_model(request: AnalyzeRequest) -> dict:
    # Example placeholder for an LLM call.
    # Replace with actual model integration and auth via environment variables.
    await asyncio.sleep(0.3)
    return {
        'summary': f'Analysis for document {request.document_id}',
        'score': 0.85,
        'tags': ['priority', 'summary'],
    }

async def analyze_document(payload: BaseModel) -> dict:
    request = AnalyzeRequest(**payload.dict())
    attempts = 0
    while attempts < 3:
        try:
            response = await call_external_model(request)
            return {
                'document_id': request.document_id,
                'summary': response['summary'],
                'score': response['score'],
                'tags': response['tags'],
                'warnings': []
            }
        except Exception as exc:
            attempts += 1
            if attempts >= 3:
                raise AnalysisError('AI provider failed after retries')
            await asyncio.sleep(2 ** attempts)

    raise AnalysisError('AI service unreachable')
