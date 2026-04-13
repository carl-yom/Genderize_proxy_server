from pydantic import BaseModel
from datetime import datetime

class ClassificationData(BaseModel):
    name: str
    gender:str
    probability : float
    sample_size : int
    is_confident : bool
    processed_at:datetime

class SuccessResponse(BaseModel):
    status:str = "success"
    data:ClassificationData

class ErrorResponse(BaseModel):
    status:str = "error"
    message:str