# Canonical Vision Document (CVD)

## Objective
Design an internal research assistant system that materially improves analyst
efficiency by automating repeatable analytical tasks, while explicitly preserving
human judgment for strategy construction, security selection, and risk assessment.

The system is intended to support an RIA/advisory research workflow and must
prioritize explainability, consistency, and auditability over speed or autonomy.

---

## Core Design Principle
**Automate discovery, diagnostics, and monitoring — not conviction.**

The system exists to:
- Reduce cognitive and time overhead
- Surface opportunities and risks earlier
- Standardize quantitative evaluation
- Make analyst judgment more visible, not hidden

---

## Layered Workflow Model

### Layer 1: Discovery (Aggressively Automated)
Purpose:
- Narrow a vast investment universe to a manageable set of candidates

Automated functions:
- Universe screening
- Strategy‑fit pre‑filters
- Valuation dispersion detection
- Factor exposure identification

Output:
- Ranked and tiered *candidates for review*, not recommendations

---

### Layer 2: Diagnostics (Standardized + Automated)
Purpose:
- Answer the same core quantitative questions consistently

Automated functions:
- Valuation snapshots (absolute and relative)
- Risk metrics (volatility, drawdown, beta, correlation)
- Factor decomposition
- Portfolio overlap and diversification impact

Output:
- A consistent quantitative dossier for each candidate

---

### Layer 3: Judgment (Human‑Only)
Purpose:
- Decide whether and why capital should be allocated

Explicitly human functions:
- Thesis formation
- Competitive advantage analysis
- Regime suitability assessment
- Risk vs. compensation evaluation
- Buy/sell conviction and kill‑criteria definition

---

## Non‑Goals
The system will not:
- Execute trades
- Generate client‑specific recommendations
- Optimize portfolios automatically
- Produce opaque or self‑optimizing “alpha scores”
- Use AI to generate investment signals

---

## Design Requirements
- Deterministic and explainable logic
- Modular architecture with clear boundaries
- Strategy‑relative evaluation
- Full transparency of assumptions
- Durable documentation for handoff

---

## Success Criteria
The system is successful if:
- Analyst screening time is reduced by >50%
- Quantitative research quality is standardized
- Risks are surfaced earlier than ad‑hoc review
- Human judgment remains explicit and defensible