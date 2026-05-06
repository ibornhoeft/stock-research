"""
metrics/risk.py

Risk metric definitions for the Metrics & Diagnostics module.

Responsibilities:
- Quantify observable risk characteristics
- Explicit mathematical definitions
- Deterministic, window-parameterized calculations

Explicit Non-Responsibilities:
- Risk preferences
- Acceptable/unacceptable thresholds
- Strategy-specific interpretation
"""

from typing import Tuple
import numpy as np
import pandas as pd


def annualized_volatility(
    log_returns: pd.Series,
    window: int,
    trading_days_per_year: int = 252,
) -> pd.Series:
    """
    Compute annualized volatility over a rolling window.

    Definition:
        sigma_ann = sqrt(trading_days_per_year) * std(r_t)

    Parameters
    ----------
    log_returns : pd.Series
        Daily log return series indexed by date.
    window : int
        Rolling window length in trading days.
    trading_days_per_year : int, default 252
        Annualization constant.

    Returns
    -------
    pd.Series
        Annualized volatility series.
        NaN for periods with insufficient history.
    """
    if window <= 0:
        raise ValueError("window must be a positive integer")

    rolling_std = log_returns.rolling(
        window=window,
        min_periods=window
    ).std()

    return np.sqrt(trading_days_per_year) * rolling_std


def maximum_drawdown(
    log_returns: pd.Series,
) -> float:
    """
    Compute maximum drawdown over the full available history.

    Definition:
        Let C_t = exp(sum_{i <= t} r_i)

        MDD = min_t ( (C_t - max_{s <= t} C_s) / max_{s <= t} C_s )

    Parameters
    ----------
    log_returns : pd.Series
        Daily log return series indexed by date.

    Returns
    -------
    float
        Maximum drawdown value (non-positive).
        Returns NaN if input is empty or all NaN.
    """
    if log_returns.dropna().empty:
        return np.nan

    cumulative = np.exp(log_returns.cumsum())
    running_max = cumulative.cummax()
    drawdowns = (cumulative - running_max) / running_max

    return drawdowns.min()


def rolling_beta(
    asset_returns: pd.Series,
    benchmark_returns: pd.Series,
    window: int,
) -> pd.Series:
    """
    Compute rolling beta relative to a benchmark.

    Definition:
        beta = cov(r_asset, r_benchmark) / var(r_benchmark)

    Assumptions:
    - asset and benchmark returns are synchronous
    - identical windows are used for covariance and variance

    Parameters
    ----------
    asset_returns : pd.Series
        Asset daily log returns.
    benchmark_returns : pd.Series
        Benchmark daily log returns.
    window : int
        Rolling window length in trading days.

    Returns
    -------
    pd.Series
        Rolling beta values.
        NaN for insufficient history or zero benchmark variance.
    """
    if window <= 0:
        raise ValueError("window must be a positive integer")

    aligned = pd.concat(
        [asset_returns, benchmark_returns],
        axis=1,
        join="inner"
    ).dropna()

    asset = aligned.iloc[:, 0]
    benchmark = aligned.iloc[:, 1]

    cov = asset.rolling(window, min_periods=window).cov(benchmark)
    var = benchmark.rolling(window, min_periods=window).var()

    beta = cov / var
    return beta