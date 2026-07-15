from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "QuantNexus"

    VERSION: str = "0.1.0"

    DEBUG: bool = True

    ANGEL_API_KEY: str = ""

    ANGEL_CLIENT_CODE: str = ""

    ANGEL_PIN: str = ""

    ANGEL_TOTP_SECRET: str = ""

    class Config:
        env_file = ".env"


settings = Settings()