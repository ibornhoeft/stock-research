"""
Local CSV provider for universe construction.

This provider loads security data from a CSV file and converts it into
canonical SecurityRecord objects.

This is the first "real" data pipeline and serves as a bridge between
stub data and production vendor data (e.g., FactSet).
"""

import csv
from datetime import datetime
from typing import List, Optional

from ..models import SecurityIdentifier, SecurityRecord


def _parse_date(value: str) -> Optional[datetime.date]:
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def _parse_bool(value: str) -> bool:
    return value.strip().lower() in {"true", "1", "yes"}


def load_securities_from_csv(filepath: str) -> List[SecurityRecord]:
    """
    Load securities from a CSV file.

    Expected columns:
    - internal_id
    - ticker
    - exchange
    - cusip
    - valid_from
    - valid_to
    - security_type
    - share_class
    - sector
    - industry
    - has_price_history
    - has_fundamentals
    """

    securities: List[SecurityRecord] = []

    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            identifier = SecurityIdentifier(
                internal_id=row["internal_id"],
                ticker=row["ticker"],
                exchange=row["exchange"],
                cusip=row["cusip"] or None,
                valid_from=_parse_date(row.get("valid_from", "")),
                valid_to=_parse_date(row.get("valid_to", "")),
            )

            record = SecurityRecord(
                identifier=identifier,
                security_type=row["security_type"],
                share_class=row["share_class"],
                sector=row.get("sector") or None,
                industry=row.get("industry") or None,
                has_price_history=_parse_bool(row["has_price_history"]),
                has_fundamentals=_parse_bool(row["has_fundamentals"]),
                metadata={},
            )

            securities.append(record)

    return securities