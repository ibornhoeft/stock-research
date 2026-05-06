"""
metrics/diagnostics.py

Pure diagnostic utilities for Metrics & Diagnostics module.

Responsibilities:
- Validate metric coverage
- Detect structural issues
- Quantify data sufficiency

NO interpretation of 'good' or 'bad'.
"""

import numpy as np
import pandas as pd


def nan_fraction(series: pd.Series) -> float:
    """
    Fraction of NaN values in a series.
    """
    if len(series) == 0:
        return np.nan
    return series.isna().mean()


def first_valid_date(series: pd.Series):
    """
    First date where the metric becomes available.
    """
    valid = series.dropna()
    return None if valid.empty else valid.index[0]


def window_coverage(
    series: pd.Series,
    window: int,
) -> pd.Series:
    """
    Boolean indicator of whether sufficient history exists
    for window-dependent metrics.

    Output:
    - True where >= window observations exist
    """
    counts = series.notna().cumsum()
    return counts >= window


def cross_correlation(
    series_a: pd.Series,
    series_b: pd.Series,
) -> float:
    """
    Simple Pearson correlation between two metric series.
    """
    aligned = pd.concat([series_a, series_b], axis=1).dropna()
    if len(aligned) < 2:
        return np.nan
    return aligned.iloc[:, 0].corr(aligned.iloc[:, 1])