"""
metrics/returns.py

Return-related metric definitions for the Metrics & Diagnostics module.

Responsibilities:
- Deterministic return calculations
- Explicit window parameterization
- No strategy interpretation or scoring logic

Interface:
- Inputs conform to Data → Metrics
- Outputs conform to Metrics → Strategy
"""

from typing import Union
import numpy as np
import pandas as pd


def daily_log_return(
    prices: pd.Series,
) -> pd.Series:
    """
    Compute daily log returns from adjusted price series.

    Definition:
        r_t = ln(P_t / P_{t-1})

    Assumptions:
    - prices are adjusted for splits and dividends upstream
    - prices are ordered by time ascending
    - prices are positive-valued

    Parameters
    ----------
    prices : pd.Series
        Adjusted close prices indexed by date.

    Returns
    -------
    pd.Series
        Daily log returns indexed by date.
        First observation will be NaN by construction.
    """
    if not isinstance(prices, pd.Series):
        raise TypeError("prices must be a pandas Series")

    log_prices = np.log(prices)
    returns = log_prices.diff()

    return returns


def rolling_cumulative_log_return(
    log_returns: pd.Series,
    window: int,
) -> pd.Series:
    """
    Compute rolling cumulative log returns over a fixed window.

    Definition:
        R_{t,W} = sum_{i=0}^{W-1} r_{t-i}

    Parameters
    ----------
    log_returns : pd.Series
        Daily log return series indexed by date.
    window : int
        Rolling window length in trading days.

    Returns
    -------
    pd.Series
        Rolling cumulative log returns.
        NaN for periods with insufficient history.
    """
    if not isinstance(log_returns, pd.Series):
        raise TypeError("log_returns must be a pandas Series")

    if window <= 0:
        raise ValueError("window must be a positive integer")

    return log_returns.rolling(window=window, min_periods=window).sum()