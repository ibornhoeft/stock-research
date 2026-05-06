"""
metrics/registry.py

Declarative registry of all Metrics & Diagnostics definitions.

Purpose:
- Enumerate available metrics
- Declare required inputs and parameters
- Provide machine-readable metadata

Explicit Non-Responsibilities:
- Executing metric logic
- Strategy relevance
- Ranking or prioritization
"""

from dataclasses import dataclass
from typing import Callable, Dict, List, Optional


@dataclass(frozen=True)
class MetricSpec:
    name: str
    function: Callable
    inputs: List[str]
    parameters: List[str]
    output: str
    family: str
    description: str


# ---- Returns ----

from metrics.returns import (
    daily_log_return,
    rolling_cumulative_log_return,
)

# ---- Risk ----

from metrics.risk import (
    annualized_volatility,
    maximum_drawdown,
    rolling_beta,
)

# ---- Valuation ----

from metrics.valuation import (
    price_to_earnings,
    price_to_book,
    ev_to_ebitda,
    historical_percentile,
)

# ---- Factors ----

from metrics.factors import (
    momentum,
    return_on_equity,
    gross_margin,
    debt_to_equity,
    yoy_growth,
)


METRIC_REGISTRY: Dict[str, MetricSpec] = {

    # ===== Returns =====
    "daily_log_return": MetricSpec(
        name="daily_log_return",
        function=daily_log_return,
        inputs=["price"],
        parameters=[],
        output="log_return",
        family="returns",
        description="Daily log return from adjusted prices.",
    ),

    "rolling_cumulative_log_return": MetricSpec(
        name="rolling_cumulative_log_return",
        function=rolling_cumulative_log_return,
        inputs=["log_return"],
        parameters=["window"],
        output="cumulative_log_return",
        family="returns",
        description="Rolling sum of log returns over a fixed window.",
    ),

    # ===== Risk =====
    "annualized_volatility": MetricSpec(
        name="annualized_volatility",
        function=annualized_volatility,
        inputs=["log_return"],
        parameters=["window", "trading_days_per_year"],
        output="volatility",
        family="risk",
        description="Annualized volatility from rolling return standard deviation.",
    ),

    "maximum_drawdown": MetricSpec(
        name="maximum_drawdown",
        function=maximum_drawdown,
        inputs=["log_return"],
        parameters=[],
        output="max_drawdown",
        family="risk",
        description="Maximum drawdown over available history.",
    ),

    "rolling_beta": MetricSpec(
        name="rolling_beta",
        function=rolling_beta,
        inputs=["log_return", "benchmark_log_return"],
        parameters=["window"],
        output="beta",
        family="risk",
        description="Rolling beta relative to benchmark.",
    ),

    # ===== Valuation =====
    "price_to_earnings": MetricSpec(
        name="price_to_earnings",
        function=price_to_earnings,
        inputs=["price", "eps"],
        parameters=[],
        output="pe_ratio",
        family="valuation",
        description="Trailing price-to-earnings multiple.",
    ),

    "price_to_book": MetricSpec(
        name="price_to_book",
        function=price_to_book,
        inputs=["price", "book_value_per_share"],
        parameters=[],
        output="pb_ratio",
        family="valuation",
        description="Price-to-book multiple.",
    ),

    "ev_to_ebitda": MetricSpec(
        name="ev_to_ebitda",
        function=ev_to_ebitda,
        inputs=["enterprise_value", "ebitda"],
        parameters=[],
        output="ev_ebitda",
        family="valuation",
        description="Enterprise value to EBITDA multiple.",
    ),

    "historical_percentile": MetricSpec(
        name="historical_percentile",
        function=historical_percentile,
        inputs=["metric_series"],
        parameters=["window"],
        output="percentile",
        family="valuation",
        description="Rolling historical percentile of a metric.",
    ),

    # ===== Factors =====
    "momentum": MetricSpec(
        name="momentum",
        function=momentum,
        inputs=["log_return"],
        parameters=["window", "skip"],
        output="momentum",
        family="factor",
        description="Lagged cumulative return momentum.",
    ),

    "return_on_equity": MetricSpec(
        name="return_on_equity",
        function=return_on_equity,
        inputs=["net_income", "shareholder_equity"],
        parameters=[],
        output="roe",
        family="factor",
        description="Return on equity.",
    ),

    "gross_margin": MetricSpec(
        name="gross_margin",
        function=gross_margin,
        inputs=["gross_profit", "revenue"],
        parameters=[],
        output="gross_margin",
        family="factor",
        description="Gross margin.",
    ),

    "debt_to_equity": MetricSpec(
        name="debt_to_equity",
        function=debt_to_equity,
        inputs=["total_debt", "shareholder_equity"],
        parameters=[],
        output="de_ratio",
        family="factor",
        description="Debt-to-equity ratio.",
    ),

    "yoy_growth": MetricSpec(
        name="yoy_growth",
        function=yoy_growth,
        inputs=["series"],
        parameters=["periods"],
        output="growth",
        family="factor",
        description="Year-over-year growth rate.",
    ),
}