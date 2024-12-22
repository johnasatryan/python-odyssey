from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator
import re
from fastapi import HTTPException

class UserCreate(BaseModel):
  username: str = Field(..., min_length=3, max_length=50)
  email: EmailStr
  password: str = Field(..., min_length=6)
  full_name: Optional[str] = ''
  image_url: Optional[str] = Field(None)
  is_admin: bool = Field(default=False)

  # @field_validator('password')
  # @classmethod
  # def validate_password(cls, value):
  #   if not re.search(r"[A-Za-z]", value):
  #     raise ValueError("Password must contain at least one letter.")
  #   if not re.search(r"\d", value):
  #     raise HTTPException(status_code=400, detail="Password must contain at least one number.")
  #   if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
  #     raise ValueError("Password must contain at least one special character.")
  #   return value
  
class UserResponse(BaseModel):
  id: int
  username: str
  email: str
  full_name: str | None
  image_url: str | None
  is_admin: bool

  class Config:
    from_attributes = True





