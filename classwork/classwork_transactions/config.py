from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    port: int

    class Config:
        env_file = ".env"

settings = Settings()
