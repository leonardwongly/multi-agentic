"""Simple FAQ retrieval tool."""
from __future__ import annotations

import difflib
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple

import yaml


LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class FAQItem:
    question: str
    answer: str


class FAQTool:
    """Load and search a YAML FAQ knowledge base."""

    def __init__(self, path: Path, *, min_similarity: float = 0.5) -> None:
        self._path = path
        self._faq = self._load(path)
        self._min_similarity = min_similarity

    @staticmethod
    def _load(path: Path) -> List[FAQItem]:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        return [FAQItem(**item) for item in data]

    def search(self, query: str, max_results: int = 1) -> List[Tuple[FAQItem, float]]:
        """Return FAQ entries ranked by similarity to the query."""

        questions = [item.question for item in self._faq]
        matches = difflib.get_close_matches(query, questions, n=max_results, cutoff=self._min_similarity)
        results: List[Tuple[FAQItem, float]] = []
        for match in matches:
            item = next(item for item in self._faq if item.question == match)
            ratio = difflib.SequenceMatcher(a=match.lower(), b=query.lower()).ratio()
            if ratio >= self._min_similarity:
                results.append((item, ratio))
        LOGGER.debug("FAQTool.search", extra={"query": query, "results": [item.question for item, _ in results]})
        return results

    def iter_items(self) -> Iterable[FAQItem]:
        return iter(self._faq)


__all__ = ["FAQTool", "FAQItem"]
