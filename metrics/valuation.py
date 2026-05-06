"""
metrics/valuation.py

Valuation-related metric definitions.

All metrics are point-in-time calculations.
No normalization, scoring, or interpretation occurs here.
"""

import numpy as np
import pandas as pd


# ---------- Multiples ----------

def price_to_earnings(
    price: pd.Series,
    earnings_per_share: pd.Series,
) -> pd.Series:
    """
    Compute trailing P/E ratio.

    Definition:
        P/E = Price / EPS

    Notes:
    - EPS may be negative; output preserved as-is
    - Inf values allowed where EPS == 0
    """
    aligned = pd.concat([price, earnings_per_share], axis=1)
    return aligned.iloc[:, 0] / aligned.iloc[:, 1]


def price_to_book(
    price: pd.Series,
    book_value_per_share: pd.Series,
) -> pd.Series:
    """
    Compute Price-to-Book ratio.
    """
    aligned = pd.concat([price, book_value_per_share], axis=1)
    return aligned.iloc[:, 0] / aligned.iloc[:, 1]


def ev_to_ebitda(
    enterprise_value: pd.Series,
    ebitda: pd.Series,
) -> pd.Series:
    """
    Compute EV / EBITDA multiple.
    """
    aligned = pd.concat([enterprise_value, ebitda], axis=1)
    return aligned.iloc[:, 0] / aligned.iloc[:, 1]


# ---------- Historical Context ----------

def historical_percentile(
    series: pd.Series,
    window: int,
) -> pd.Series:
    """
    Compute rolling historical percentile of current value
    relative to its own history.

    Definition:
        percentile_t = rank(series_t within [t-W+1, ..., t]) / W

    Output:
    - Range: [0, 1]
    """
    if window <= 0:
        raise ValueError("window must be positive")

    def pct_rank(x):
        return x.rank(pct=True).iloc[-1]

    return series.rolling(window, min_periods=window).apply(pct_rank, raw=False)