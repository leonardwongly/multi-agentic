"""Mock LLM implementation used for deterministic tests."""
from __future__ import annotations

import textwrap
from typing import Dict

from .base import LanguageModel


class MockLLM(LanguageModel):
    """A tiny deterministic model that formats templated responses."""

    def __init__(self, templates: Dict[str, str] | None = None) -> None:
        self._templates = templates or {}

    def register(self, key: str, template: str) -> None:
        self._templates[key] = template

    def complete(self, *, prompt: str, key: str | None = None, **kwargs: object) -> str:
        template = self._templates.get(key or "default", "{prompt}")
        return textwrap.dedent(template).format(prompt=prompt, **kwargs).strip()


__all__ = ["MockLLM"]
