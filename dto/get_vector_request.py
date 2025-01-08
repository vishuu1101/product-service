from pydantic import BaseModel

class GetVectorRequest(BaseModel):
    search_text: str