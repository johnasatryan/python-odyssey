from sqlalchemy.orm import validates
from sqlalchemy import Column, Integer, String, Text, Boolean

from db import Base


class UserDB(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(50), nullable=False)
  password = Column(String(50), nullable=False)
  email = Column(String(50), unique=True, nullable=False)
  image_url = Column(Text, nullable=True)
  full_name = Column(Text, nullable=True)
  is_admin = Column(Boolean, default=False)

  @validates('username')
  def validate_username(self, key, username):
    if len(username) <= 3:
      raise ValueError("Username needs to be longer")
    return username