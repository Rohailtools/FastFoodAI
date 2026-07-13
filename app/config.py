from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str = "FastFood AI v2"

    APP_VERSION: str = "2.0.0"

    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
