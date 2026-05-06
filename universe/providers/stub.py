"""
Stub provider for development and testing.

This provider intentionally includes edge cases to validate universe logic.
"""

from datetime import date
from typing import List

from ..models import SecurityIdentifier, SecurityRecord


def load_stub_securities() -> List[SecurityRecord]:
    """
    Returns a small, deterministic set of Securities for testing.

    Includes:
    - Valid common equity
    - Invalid exchange
    - Missing price history
    """

    return [
        SecurityRecord(
            identifier=SecurityIdentifier(
                internal_id="SEC-0001",
                ticker="ABC",
                exchange="NYSE",
                cusip="000000001",
                valid_from=date(2010, 1, 1),
            ),
            security_type="COMMON_STOCK",
            share_class="ORD",
            sector="Technology",
            industry="Software",
            has_price_history=True,
            has_fundamentals=True,
        ),
        SecurityRecord(
            identifier=SecurityIdentifier(
                internal_id="SEC-0002",
                ticker="XYZ",
                exchange="OTC",
                cusip=None,
            ),
            security_type="COMMON_STOCK",
            share_class="ORD",
            has_price_history=True,
        ),
        SecurityRecord(
            identifier=SecurityIdentifier(
                internal_id="SEC-0003",
                ticker="NOPRICE",
                exchange="NASDAQ",
                cusip=None,
            ),
            security_type="COMMON_STOCK",
            share_class="ORD",
            has_price_history=False,
        ),
    ]