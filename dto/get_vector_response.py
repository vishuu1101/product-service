from typing import List
from pydantic import BaseModel

class GetVectorResponse(BaseModel):
    embedding: List[float]