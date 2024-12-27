from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    target_db: str
    default_db: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    app_port: int

    class Config:
        env_file = ".env"

settings = Settings()
