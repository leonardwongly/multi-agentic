"""LangGraph workflow for the support use case."""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Iterable

from langchain_core.messages import HumanMessage
from langgraph.graph import END, StateGraph

from .agents.intake import IntakeAgent
from .agents.knowledge import KnowledgeAgent
from .agents.resolution import ResolutionAgent
from .logging_utils import configure_logging
from .state import TicketState, initial_state

LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class SupportWorkflow:
    """Compile and execute the support workflow graph."""

    intake: IntakeAgent
    knowledge: KnowledgeAgent
    resolution: ResolutionAgent
    _graph: object = field(init=False, repr=False)

    def __post_init__(self) -> None:
        configure_logging()
        graph = StateGraph(TicketState)
        graph.add_node("intake", self.intake.run)
        graph.add_node("knowledge", self.knowledge.run)
        graph.add_node("resolution", self.resolution.run)

        graph.set_entry_point("intake")
        graph.add_edge("intake", "knowledge")
        graph.add_edge("knowledge", "resolution")
        graph.add_edge("resolution", END)

        self._graph = graph.compile()

    def run(self, *, messages: Iterable[str]) -> TicketState:
        """Execute the workflow for the provided user messages."""

        history = [HumanMessage(content=msg, name="customer") for msg in messages]
        state = initial_state(history)
        LOGGER.info("Starting workflow", extra={"messages": len(history)})
        result = self._graph.invoke(state)
        LOGGER.info("Workflow complete", extra={"resolution": result.get("resolution")})
        return result


__all__ = ["SupportWorkflow"]
