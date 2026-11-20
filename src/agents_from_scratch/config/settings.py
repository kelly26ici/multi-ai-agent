from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).resolve().parents[3]
ENV_PATH = PROJECT_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    nvidia_api_key: SecretStr
    default_model: str = Field(default="nvidia:nvidia/nemotron-3.5-lightning-30b-a3b")
    temperature: float = Field(default=0.2, ge=0.00, le=2.0)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached application settings."""
    return Settings()


settings = get_settings()
