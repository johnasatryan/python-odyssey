from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserModel(BaseModel):
  _id: Optional[int] = None
  username: str = Field(..., min_length=4, max_length=50)
  email: EmailStr
  password: str = Field(..., min_length=6)
  full_name: Optional[str] = Field(min_length=4)
  image_url: Optional[str] = None
  is_admin: bool = False