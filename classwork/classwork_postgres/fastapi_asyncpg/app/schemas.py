from pydantic import BaseModel, Field, EmailStr

from typing import Optional

class UserModel(BaseModel):
  id:Optional[int]= None
  username:str = Field(...,min_length=3, max_length=50)
  password:str= Field(...,min_length=6 )
  email:EmailStr
  image_url:Optional[str]= None
  full_name:Optional[str]
  is_admin:bool = False
  class Config:
    orm_mode = True

    
