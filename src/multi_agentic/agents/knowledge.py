"""Agent that queries the FAQ knowledge base."""
from __future__ import annotations

from ..llm.base import LanguageModel
from ..state import TicketState
from ..tools.faq_tool import FAQTool
from .base import Agent


class KnowledgeAgent(Agent):
    """Recommend solutions using FAQ search results."""

    def __init__(self, model: LanguageModel, tool: FAQTool) -> None:
        super().__init__(name="knowledge", model=model)
        self._tool = tool

    def run(self, state: TicketState) -> TicketState:
        query = state.get("original_issue") or state.get("customer_issue") or ""
        results = self._tool.search(query, max_results=1)
        if not results:
            response = self.model.complete(prompt=query, key="knowledge_missing")
            state["proposed_solution"] = None
        else:
            item, score = results[0]
            response = self.model.complete(
                prompt=query,
                key="knowledge",
                question=item.question,
                answer=item.answer,
                score=score,
            )
            state["proposed_solution"] = item.answer
        self._append_message(state, response)
        return state


__all__ = ["KnowledgeAgent"]
