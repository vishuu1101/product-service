from typing import List
from pydantic import BaseModel

class AddProductResponse(BaseModel):
    name: str
    desc: str
    searchText: str
    category: str
    price: float
    embedding: List[float]