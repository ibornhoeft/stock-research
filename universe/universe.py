"""
Universe construction logic.

Coordinates providers and filters to produce a clean, deterministic universe.
"""

from datetime import date
from typing import Iterable

from .models import Universe, SecurityRecord
from .filters import (
    filter_by_exchange,
    filter_by_security_type,
    filter_by_data_availability,
)


def build_universe(
    securities: Iterable[SecurityRecord],
    as_of_date: date,
) -> Universe:
    """
    Construct a universe from raw SecurityRecord inputs.

    Parameters
    ----------
    securities:
        Iterable of canonical SecurityRecord objects.
    as_of_date:
        Effective date of the universe snapshot.

    Returns
    -------
    Universe
        A filtered, structurally valid investment universe.
    """

    filtered = filter_by_exchange(securities)
    filtered = filter_by_security_type(filtered)
    filtered = filter_by_data_availability(filtered)

    return Universe(
        as_of_date=as_of_date,
        securities=list(filtered),
    )