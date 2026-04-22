# Interface: Metrics → Strategy Logic

## Inputs
- Computed metrics (returns, risk, valuation, factors)
- Time-window definitions

## Outputs
- Metric snapshots and histories suitable for evaluation

## Assumptions
- Metrics are deterministic
- Metric definitions are frozen before strategy application

## Non-Responsibilities
- Ranking
- Output formatting