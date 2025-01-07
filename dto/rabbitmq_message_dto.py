from pydantic import BaseModel

class MessageDTO(BaseModel):
    pattern: str
    data: str