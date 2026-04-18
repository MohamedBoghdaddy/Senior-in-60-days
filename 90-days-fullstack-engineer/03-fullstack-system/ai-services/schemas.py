from pydantic import BaseModel, Field

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
