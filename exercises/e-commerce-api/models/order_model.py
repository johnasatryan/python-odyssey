from pydantic import BaseModel,Field
from typing import Optional, List
from enum import Enum


class Status(Enum):
  PENDING = 0
  ARRIVING = 1
  DELIVERED = 2

class OrderItem(BaseModel):
  product_id: int 
  quantity:int = Field(...,gt=0)

class OrderModel(BaseModel):
  _id: Optional[int] = None
  user_id:int
  items: List[OrderItem]
  total_price: float = Field(...,gt=0)
  status:str = Field(default=Status.PENDING) 
