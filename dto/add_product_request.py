from pydantic import BaseModel, Field

class AddProductRequest(BaseModel):
    name: str = Field(..., min_length=1, description="Name must not be blank")
    desc: str = Field(..., min_length=1, description="Desc must not be blank")
    searchText: str = Field(..., min_length=1, description="SearchText must not be blank")
    category: str = Field(..., min_length=1, description="Category must not be blank")
    price: float = Field(..., gt=0, lt=10000, description="Price must be greater than 0 and less than 10,000")