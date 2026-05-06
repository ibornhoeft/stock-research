"""
FactSet provider adapter (placeholder).

This file intentionally contains no implementation and no credentials.
It exists to lock in the adapter interface early.
"""

from typing import List
from ..models import SecurityRecord


class FactSetProvider:
    """
    Adapter for FactSet security master data.

    TODO:
    - Authenticate using firm credentials
    - Load security master and corporate actions
    - Map FactSet identifiers to canonical SecurityRecord objects
    """

    def load(self) -> List[SecurityRecord]:
        raise NotImplementedError("FactSet provider not implemented yet.")