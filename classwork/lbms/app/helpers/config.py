from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
  PORT: int
  MONGO_URI: str
  ACCESS_TOKEN_EXPIRE_MINUTES: int
  SECRET_KEY: str
  ALGORITHM: str

  class Config:
    env_file = '.env'

settings = Settings()
