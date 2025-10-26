"""LLM interface definitions."""
from __future__ import annotations

from typing import Protocol


class LanguageModel(Protocol):
    """Protocol for simple language model implementations."""

    def complete(self, *, prompt: str, **kwargs: object) -> str:
        """Return a completion for the provided prompt."""


__all__ = ["LanguageModel"]
