from pydantic import BaseModel,Field
from typing import Optional

class ProductModel(BaseModel):
  _id: Optional[int] = None
  name: str = Field(..., min_length=1, max_length=100)
  description: Optional[str] = None
  price: float = Field(..., gt=0)
  category: Optional[str] = None
  image_url: Optional[str] = None
  is_active: bool = True
