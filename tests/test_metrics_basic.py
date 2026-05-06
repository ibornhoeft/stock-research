import numpy as np
import pandas as pd

from metrics.returns import daily_log_return
from metrics.risk import annualized_volatility, maximum_drawdown
from metrics.factors import momentum
from metrics.valuation import historical_percentile


def test_daily_log_return_identity():
    prices = pd.Series([100, 100, 100])
    r = daily_log_return(prices)
    assert np.isnan(r.iloc[0])
    assert r.iloc[1] == 0.0
    assert r.iloc[2] == 0.0


def test_annualized_volatility_zero():
    returns = pd.Series([0.0] * 300)
    vol = annualized_volatility(returns, window=252)
    assert vol.dropna().iloc[-1] == 0.0


def test_maximum_drawdown_monotonic_up():
    returns = pd.Series([0.01] * 100)
    mdd = maximum_drawdown(returns)
    assert mdd == 0.0


def test_momentum_basic():
    returns = pd.Series([0.01] * 20)
    mom = momentum(returns, window=10)
    assert np.isclose(mom.dropna().iloc[-1], 0.10)


def test_historical_percentile_bounds():
    series = pd.Series(range(100))
    pct = historical_percentile(series, window=20)
    assert pct.dropna().between(0.0, 1.0).all()