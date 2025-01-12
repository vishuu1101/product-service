from typing import List
from pydantic import BaseModel

class AddProductResponse(BaseModel):
    name: str
    pvid: str
    pmid: str
    searchText: str
    category: str
    price: float
    embedding: List[float]