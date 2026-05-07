"""
metrics/stability.py

Stability metrics quantify how a metric evolves over time.

These are second-order properties:
    -> Not the metric itself
    -> But how stable or volatile it is

No interpretation is applied.
"""

import pandas as pd


def rolling_std(series: pd.Series, window: int) -> pd.Series:
    """
    Rolling standard deviation of a metric.
    """
    return series.rolling(window, min_periods=window).std()


def rolling_mean(series: pd.Series, window: int) -> pd.Series:
    """
    Rolling mean of a metric.
    """
    return series.rolling(window, min_periods=window).mean()


def coefficient_of_variation(series: pd.Series, window: int) -> pd.Series:
    """
    Coefficient of variation = std / mean
    """
    mean = rolling_mean(series, window)
    std = rolling_std(series, window)
    return std / mean