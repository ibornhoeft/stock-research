from dataclasses import dataclass, field
from datetime import date
from typing import Optional, Dict, Any, List


@dataclass(frozen=True)
class SecurityIdentifier:
    """
    Canonical, time-aware security identity.

    This object exists to prevent silent ticker reuse and identity ambiguity.
    """

    internal_id: str                    # Permanent, never reused
    ticker: str                         # Exchange ticker (point-in-time aware)
    exchange: str                       # NYSE, NASDAQ, NYSEAM
    cusip: Optional[str]                # May be None

    valid_from: Optional[date] = None
    valid_to: Optional[date] = None


@dataclass
class SecurityRecord:
    """
    Canonical representation of a security eligible for universe consideration.

    Contains no metrics, rankings, or strategy interpretation.
    """

    identifier: SecurityIdentifier

    # Structural classification
    security_type: str                  # e.g. "COMMON_STOCK"
    share_class: str                    # e.g. "ORD", "A", "B"

    # Descriptive metadata
    name: Optional[str] = None          # Optional company name
    sector: Optional[str] = None
    industry: Optional[str] = None

    # Data availability flags (never inferred downstream)
    has_price_history: bool = False
    has_fundamentals: bool = False

    # Provider-specific diagnostics (opaque to this module)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Universe:
    """
    Container for a fully constructed investment universe.
    """

    as_of_date: date
    securities: List[SecurityRecord]