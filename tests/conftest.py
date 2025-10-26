"""Pytest configuration for test suite."""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure the project root (containing the src/ directory) is on sys.path so that
# ``import multi_agentic`` works when the package is not installed in editable mode.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
