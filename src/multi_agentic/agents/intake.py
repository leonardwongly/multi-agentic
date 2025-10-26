"""Agent responsible for capturing the customer's problem."""
from __future__ import annotations

from langchain_core.messages import HumanMessage

from ..llm.base import LanguageModel
from ..state import TicketState
from .base import Agent


class IntakeAgent(Agent):
    """Summarise the customer's request into a structured problem statement."""

    def __init__(self, model: LanguageModel) -> None:
        super().__init__(name="intake", model=model)

    def run(self, state: TicketState) -> TicketState:
        history = state.get("history", [])
        latest_human = next((msg for msg in reversed(history) if isinstance(msg, HumanMessage)), None)
        issue_text = latest_human.content if latest_human else ""
        summary = self.model.complete(
            prompt=issue_text,
            key="intake",
            summary="Customer reports: {issue}".format(issue=issue_text),
        )
        state["original_issue"] = issue_text
        state["customer_issue"] = summary
        self._append_message(state, summary)
        return state


__all__ = ["IntakeAgent"]
