"""Logging configuration helpers."""
from __future__ import annotations

import logging
from typing import Optional


def configure_logging(level: int | str = logging.INFO, handler: Optional[logging.Handler] = None) -> None:
    """Configure the root logger for the demo application."""

    logging.basicConfig(level=level, handlers=[handler] if handler else None)


__all__ = ["configure_logging"]
