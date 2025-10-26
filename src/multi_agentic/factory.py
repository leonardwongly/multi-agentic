"""Factory utilities to assemble the workflow."""
from __future__ import annotations

from pathlib import Path

from .agents.intake import IntakeAgent
from .agents.knowledge import KnowledgeAgent
from .agents.resolution import ResolutionAgent
from .coordinator import SupportWorkflow
from .llm.mock import MockLLM
from .tools.faq_tool import FAQTool

DEFAULT_TEMPLATES = {
    "intake": "{summary}",
    "knowledge": "Matched FAQ: {question}\nConfidence: {score:.2f}\nRecommended steps: {answer}",
    "knowledge_missing": "No relevant FAQ found. Escalating to support specialist.",
    "resolution": "Summary: {summary}\n\nSolution:\n{solution}\n\nLet us know if you need further assistance.",
}


def build_mock_workflow(knowledge_base_path: Path | None = None) -> SupportWorkflow:
    """Create a support workflow using the mock language model."""

    model = MockLLM(DEFAULT_TEMPLATES)
    tool = FAQTool(knowledge_base_path or Path(__file__).resolve().parent / "data" / "faq.yml")
    intake = IntakeAgent(model)
    knowledge = KnowledgeAgent(model, tool)
    resolution = ResolutionAgent(model)
    return SupportWorkflow(intake=intake, knowledge=knowledge, resolution=resolution)


__all__ = ["build_mock_workflow"]
