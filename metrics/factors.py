"""
metrics/factors.py

Factor-style metric definitions.

These are *raw factor measurements* only.
No weighting, aggregation, or strategy usage occurs here.
"""

import numpy as np
import pandas as pd


# ---------- Momentum ----------

def momentum(
    log_returns: pd.Series,
    window: int,
    skip: int = 0,
) -> pd.Series:
    """
    Compute momentum as rolling cumulative log return,
    optionally skipping most recent observations.

    Definition:
        Momentum_t = sum(r_{t-k-W+1} ... r_{t-k})
    """
    if window <= 0:
        raise ValueError("window must be positive")

    shifted = log_returns.shift(skip)
    return shifted.rolling(window, min_periods=window).sum()


# ---------- Profitability ----------

def return_on_equity(
    net_income: pd.Series,
    shareholder_equity: pd.Series,
) -> pd.Series:
    """
    ROE = Net Income / Shareholder Equity
    """
    aligned = pd.concat([net_income, shareholder_equity], axis=1)
    return aligned.iloc[:, 0] / aligned.iloc[:, 1]


def gross_margin(
    gross_profit: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """
    Gross Margin = Gross Profit / Revenue
    """
    aligned = pd.concat([gross_profit, revenue], axis=1)
    return aligned.iloc[:, 0] / aligned.iloc[:, 1]


# ---------- Leverage ----------

def debt_to_equity(
    total_debt: pd.Series,
    shareholder_equity: pd.Series,
) -> pd.Series:
    """
    Debt-to-Equity ratio.
    """
    aligned = pd.concat([total_debt, shareholder_equity], axis=1)
    return aligned.iloc[:, 0] / aligned.iloc[:, 1]


# ---------- Growth ----------

def yoy_growth(
    series: pd.Series,
    periods: int = 1,
) -> pd.Series:
    """
    Year-over-year style growth rate.

    Definition:
        Growth = (X_t / X_{t-periods}) - 1
    """
    return series / series.shift(periods) - 1.0

def asset_turnover(revenue: pd.Series, total_assets: pd.Series):
    return revenue / total_assets


def operating_margin(operating_income: pd.Series, revenue: pd.Series):
    return operating_income / revenue


def free_cash_flow_yield(fcf: pd.Series, market_cap: pd.Series):
    return fcf / market_cap