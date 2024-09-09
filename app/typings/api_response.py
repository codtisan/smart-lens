from pydantic import BaseModel
from datetime import datetime

class HealthResponse(BaseModel):
    status: str
    status_code: int
    timestamp: datetime

class OCRResult(BaseModel):
    text: str
    
class OCRResponse(BaseModel):
    status: str
    status_code: int
    timestamp: datetime
    result: OCRResult


