"""Base agent abstraction."""
from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from langchain_core.messages import AIMessage

from ..llm.base import LanguageModel
from ..state import TicketState

LOGGER = logging.getLogger(__name__)


class Agent(ABC):
    """Interface implemented by workflow agents."""

    def __init__(self, name: str, model: LanguageModel) -> None:
        self.name = name
        self.model = model

    @abstractmethod
    def run(self, state: TicketState) -> TicketState:
        """Execute the agent and return the updated state."""

    def _append_message(self, state: TicketState, content: str) -> None:
        LOGGER.info("%s response: %s", self.name, content)
        history = state.setdefault("history", [])
        history.append(AIMessage(content=content, name=self.name))


__all__ = ["Agent"]
