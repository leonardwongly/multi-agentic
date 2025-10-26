"""Unit tests for the support workflow."""
from __future__ import annotations

import pytest

from multi_agentic.factory import build_mock_workflow


@pytest.fixture()
def workflow():
    return build_mock_workflow()


def test_workflow_resolves_printer_issue(workflow):
    state = workflow.run(messages=["The printer on floor 3 is jammed again."])
    assert state["finished"] is True
    assert "printer" in state["customer_issue"].lower()
    assert "Power off the printer" in state["proposed_solution"]


def test_workflow_handles_unknown_issue(workflow):
    state = workflow.run(messages=["My desk chair squeaks."])
    assert state["finished"] is True
    assert "escalating" in state["history"][-2].content.lower() or "escalating" in state["history"][-1].content.lower()
