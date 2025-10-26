"""CLI entry point for the multi-agent demo."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer

from .config import get_settings
from .factory import build_mock_workflow

app = typer.Typer(help="Demonstration multi-agent support workflow")


@app.command()
def demo(
    message: str = typer.Option(
        ..., "--message", "-m", help="Customer issue to process"
    ),
    knowledge_base: Optional[Path] = typer.Option(
        None, "--kb", help="Optional path to FAQ knowledge base"
    ),
) -> None:
    """Run the workflow for a single customer message."""

    settings = get_settings()
    workflow = build_mock_workflow(knowledge_base_path=knowledge_base or settings.knowledge_base_path)
    result = workflow.run(messages=[message])
    typer.echo(json.dumps(result, indent=2, default=str))


def main():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":  # pragma: no cover
    main()
