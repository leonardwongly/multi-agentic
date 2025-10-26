"""State models used by the LangGraph workflow."""
from __future__ import annotations

from typing import List, Optional, TypedDict

from langchain_core.messages import BaseMessage


class TicketState(TypedDict, total=False):
    """State shared between agents in the workflow."""

    history: List[BaseMessage]
    original_issue: Optional[str]
    customer_issue: Optional[str]
    proposed_solution: Optional[str]
    resolution: Optional[str]
    finished: bool


def initial_state(history: List[BaseMessage]) -> TicketState:
    return TicketState(
        history=history,
        original_issue=None,
        customer_issue=None,
        proposed_solution=None,
        resolution=None,
        finished=False,
    )


__all__ = ["TicketState", "initial_state"]
