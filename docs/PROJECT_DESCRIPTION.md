# Project Description: Research Assistant Platform

## What This Project Is

This project is an internal research assistant platform designed to support
investment analysts in an RIA / advisory context.

Its purpose is to automate *repeatable analytical tasks* while preserving
human judgment where it matters: strategy construction, security selection,
risk assessment, and conviction.

The system is intentionally AI‑free at its foundation and is built to be
deterministic, explainable, modular, and auditable.

---

## What the System Does

The system supports analysts by:

- Narrowing large universes of securities into manageable candidate sets
- Standardizing quantitative diagnostics across ideas
- Evaluating securities relative to explicit portfolio strategies
- Monitoring holdings for structural deterioration or opportunity cost

It automates:
- Discovery
- Diagnostics
- Monitoring

It does **not** automate:
- Conviction
- Recommendations
- Trades
- Client-specific guidance

---

## Conceptual Workflow

Universe → Metrics → Strategy Logic → Ranking → Outputs

Each stage has a single responsibility and communicates with the next via
explicit interface contracts.

---

## Intended Users

- Internal research analysts
- Portfolio strategists
- Advisors seeking consistent analytical support

---

## Design Philosophy

- Explainability over optimization
- Consistency over cleverness
- Judgment amplification, not replacement
- Documentation as first-class infrastructure

---

## Longevity Goals

The system is designed to:
- Survive analyst turnover
- Survive AI tooling changes
- Survive loss of a specific Copilot subscription
- Be understandable by new contributors with minimal ramp-up