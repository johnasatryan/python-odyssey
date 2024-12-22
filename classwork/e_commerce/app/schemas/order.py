from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class OrderItemCreate(BaseModel):
    product_id: int = Field(..., gt=0) 
    quantity: int = Field(..., gt=0) 

class OrderCreate(BaseModel):
    user_id: int = Field(..., gt=0) 
    items: List[OrderItemCreate]  
    status: str = Field("PENDING", pattern="^(PENDING|ARRIVING|DELIVERED)$") 



class OrderItemResponse(BaseModel):
    id: int 
    product_id: int
    quantity: int
    price: float 

    class Config:
        orm_mode = True

        
class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: str
    created_at: datetime
    items: List[OrderItemResponse]  

    class Config:
        orm_mode = True
