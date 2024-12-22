from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = None  
    price: float = Field(..., gt=0)  
    category: str | None = Field(None, max_length=50)  
    image_url: str | None = None  


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    category: str | None
    image_url: str | None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  
