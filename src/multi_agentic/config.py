"""Configuration utilities for the multi-agent workflow."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    openai_api_key: Optional[str] = Field(
        default=None,
        description="API key used for OpenAI integrations. Optional because the demo uses a mock LLM.",
    )
    knowledge_base_path: Path = Field(
        default=Path(__file__).resolve().parent / "data" / "faq.yml",
        description="Location of the FAQ knowledge base file.",
    )

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return cached application settings."""

    return Settings()


__all__ = ["Settings", "get_settings"]
