"""
Structural filters applied during universe construction.

These filters enforce eligibility constraints but never evaluate quality,
attractiveness, or strategy fit.
"""

from typing import Iterable, List
from .models import SecurityRecord


APPROVED_EXCHANGES = {"NYSE", "NASDAQ", "NYSEAM"}
ALLOWED_SECURITY_TYPES = {"COMMON_STOCK"}


def filter_by_exchange(
    securities: Iterable[SecurityRecord],
) -> List[SecurityRecord]:
    return [
        s for s in securities
        if s.identifier.exchange in APPROVED_EXCHANGES
    ]


def filter_by_security_type(
    securities: Iterable[SecurityRecord],
) -> List[SecurityRecord]:
    return [
        s for s in securities
        if s.security_type in ALLOWED_SECURITY_TYPES
    ]


def filter_by_data_availability(
    securities: Iterable[SecurityRecord],
) -> List[SecurityRecord]:
    """
    Enforces structural data continuity requirements.
    Does NOT attempt to repair or infer missing data.
    """
    return [
        s for s in securities
        if s.has_price_history
    ]