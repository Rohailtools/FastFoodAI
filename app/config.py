from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "FastFood AI"

    APP_VERSION: str = "2.0.0"

    DEBUG: bool = True

    SUPABASE_URL: str

    SUPABASE_ANON_KEY: str

    SUPABASE_SERVICE_KEY: str

    GROQ_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
