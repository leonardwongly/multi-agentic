"""Agent that finalises the ticket response."""
from __future__ import annotations

from ..llm.base import LanguageModel
from ..state import TicketState
from .base import Agent


class ResolutionAgent(Agent):
    """Provide final response and mark workflow as complete."""

    def __init__(self, model: LanguageModel) -> None:
        super().__init__(name="resolution", model=model)

    def run(self, state: TicketState) -> TicketState:
        response = self.model.complete(
            prompt=state.get("proposed_solution") or state.get("customer_issue") or "",
            key="resolution",
            summary=state.get("customer_issue") or "",
            solution=state.get("proposed_solution") or "We are escalating your ticket to a specialist.",
        )
        state["resolution"] = response
        state["finished"] = True
        self._append_message(state, response)
        return state


__all__ = ["ResolutionAgent"]
