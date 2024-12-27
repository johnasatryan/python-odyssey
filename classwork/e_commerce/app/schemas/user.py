from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
  username: str = Field(..., min_length=3, max_length=50)
  email: EmailStr
  password: str = Field(..., min_length=6)
  full_name: Optional[str] = ''
  image_url: Optional[str] = Field(None)
  is_admin: bool = Field(default=False)

  
class UserResponse(BaseModel):
  id: int
  username: str
  email: str
  full_name: str | None
  image_url: str | None
  is_admin: bool

  class Config:
    from_attributes = True





