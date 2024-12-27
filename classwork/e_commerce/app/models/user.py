from sqlalchemy import Column, Integer, String, Boolean, Text, TIMESTAMP
from sqlalchemy.sql import func
from models.base import Base


class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(50), unique=True, nullable=False)
  email = Column(String(100), unique=True, nullable=False)
  password = Column(String(255), nullable=False)
  full_name = Column(String(100), nullable=True)
  image_url = Column(Text, nullable=True)
  is_admin = Column(Boolean, default=False)
  created_at = Column(TIMESTAMP, server_default=func.now())


  