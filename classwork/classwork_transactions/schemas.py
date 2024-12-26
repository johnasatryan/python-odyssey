from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AccountCreate(BaseModel):
    name: str = Field(..., max_length=100, description="Name of the account holder")
    balance: Optional[float] = Field(default=0.00, description="Initial balance")

class AccountResponse(BaseModel):
    id: int
    name: str
    balance: float

    class Config:
        from_attributes = True

class TransactionCreate(BaseModel):
    sender_id: int = Field(..., description="ID of the sender's account")
    receiver_id: int = Field(..., description="ID of the receiver's account")
    amount: float = Field(..., gt=0, description="Amount to transfer")

class TransactionResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    amount: float
    timestamp: datetime

    class Config:
        from_attributes = True
