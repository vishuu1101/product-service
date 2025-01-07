from pydantic import BaseModel

class AddProductResponse(BaseModel):
    name: str