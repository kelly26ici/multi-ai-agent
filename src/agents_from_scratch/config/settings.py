from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).resolve().parents[3]
ENV_PATH = PROJECT_DIR / ".env"


class AgentModels(BaseModel):
    """Model names for the supervisor, each subagent, and general use."""

    default_model: str = Field(description="Model for general use.")
    supervisor_model: str = Field(description="Model for the supervisor agent.")
    researcher_model: str = Field(description="Model for the researcher subagent.")
    email_writer_model: str = Field(description="Model for the email writer subagent.")


class AgentTemperatures(BaseModel):
    """Sampling temperature for the supervisor and each subagent."""

    default: float = Field(default=0.2, ge=0.0, le=2.0)
    supervisor: float = Field(default=0.2, ge=0.0, le=2.0)
    researcher: float = Field(default=0.2, ge=0.0, le=2.0)
    email_writer: float = Field(default=0.2, ge=0.0, le=2.0)


class Provider(BaseModel):
    """API key, models, and temperatures for one model provider."""

    api_key: SecretStr | None = None
    models: AgentModels
    temperature: AgentTemperatures = AgentTemperatures()


class Settings(BaseSettings):
    """One settings block per provider, nested with the `__` delimiter.

    Example environment entries:
        NVIDIA__API_KEY=...
        NVIDIA__MODELS__SUPERVISOR_MODEL=...
        NVIDIA__TEMPERATURE__RESEARCHER=0.1
    """

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    nvidia: Provider = Provider(
        models=AgentModels(
            default_model="nvidia:nvidia/nemotron-3.5-lightning-30b-a3b",
            supervisor_model="nvidia:nvidia/nemotron-3.5-lightning-30b-a3b",
            researcher_model="nvidia:nvidia/nemotron-3.5-lightning-30b-a3b",
            email_writer_model="nvidia:nvidia/nemotron-3.5-lightning-30b-a3b",
        )
    )
    anthropic: Provider = Provider(
        models=AgentModels(
            default_model="anthropic:claude-sonnet-4-5",
            supervisor_model="anthropic:claude-sonnet-4-5",
            researcher_model="anthropic:claude-sonnet-4-5",
            email_writer_model="anthropic:claude-sonnet-4-5",
        )
    )
    gemini: Provider = Provider(
        models=AgentModels(
            default_model="google_genai:gemini-2.5-pro",
            supervisor_model="google_genai:gemini-2.5-pro",
            researcher_model="google_genai:gemini-2.5-pro",
            email_writer_model="google_genai:gemini-2.5-pro",
        )
    )
    ollama: Provider = Provider(
        models=AgentModels(
            default_model="ollama:llama3.1",
            supervisor_model="ollama:llama3.1",
            researcher_model="ollama:llama3.1",
            email_writer_model="ollama:llama3.1",
        )
    )
    openai: Provider = Provider(
        models=AgentModels(
            default_model="openai:gpt-5-mini",
            supervisor_model="openai:gpt-5-mini",
            researcher_model="openai:gpt-5-mini",
            email_writer_model="openai:gpt-5-mini",
        )
    )
    openrouter: Provider = Provider(
        models=AgentModels(
            default_model="openrouter:openai/gpt-5-mini",
            supervisor_model="openrouter:openai/gpt-5-mini",
            researcher_model="openrouter:openai/gpt-5-mini",
            email_writer_model="openrouter:openai/gpt-5-mini",
        )
    )
    tavily_api_key: SecretStr | None = None
    exa_api_key: SecretStr | None = None
    firecrawl_api_key: SecretStr | None = None
    diffbot_api_key: SecretStr | None = None
    serpapi_api_key: SecretStr | None = None
    linkup_api_key: SecretStr | None = None
    keenable_api_key: SecretStr | None = None
    querit_api_key: SecretStr | None = None
    crustapi_api_key: SecretStr | None = None
    cloro_api_key: SecretStr | None = None
    agentsearch_api_key: SecretStr | None = None


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached application settings."""
    return Settings()


settings = get_settings()
