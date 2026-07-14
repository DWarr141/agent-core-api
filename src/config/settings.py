"""Settings for the application."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    api_name: str = "Agent Core API"
    api_version: str = "1.0.0"
    app_env: str = "development"
    debug: bool = False

    minimax_api_key: str | None = None
    minimax_base_url: str = "https://api.minimax.io/v1"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
