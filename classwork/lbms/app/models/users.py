from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
  username: str
  email: EmailStr
  password: str
  is_active: bool = True

class UserIn(BaseModel):
  email: EmailStr
  password: str

class UserOut(UserBase):
  id: str
  username: str


