# System Architecture Document

## Purpose
This document defines the logical architecture of the research assistant system.
It specifies module boundaries, responsibilities, and data flow, and serves as
the authoritative reference for how different parts of the system interact.

All implementation decisions must respect the boundaries defined here.

---

## High-Level Architecture Overview

The system is organized as a **linear, modular pipeline** that mirrors the
analyst workflow:

Universe → Metrics → Strategy Logic → Ranking → Outputs

Each stage:
- Has a clearly defined responsibility
- Consumes inputs only from the prior stage
- Produces explicit, inspectable outputs

No stage is permitted to “reach across” layers.

---

## Core Modules and Responsibilities

### 1. Data & Universe Module
**Purpose:** Define *what* is eligible for consideration.

Responsibilities:
- Universe definitions (e.g., U.S. equities)
- Inclusion and exclusion rules
- Structural constraints (liquidity, market cap, etc.)
- Documentation of data assumptions and limitations

Outputs:
- A clean universe of securities
- Standardized identifiers and metadata

Explicitly Not Responsible For:
- Computing metrics
- Evaluating “quality” or “attractiveness”
- Strategy fit or ranking

---

### 2. Metrics & Diagnostics Module
**Purpose:** Quantify observable properties of securities.

Responsibilities:
- Return calculations
- Risk metrics (volatility, drawdown, beta, correlations)
- Valuation transformations
- Factor decompositions

Outputs:
- Deterministic, reproducible metric tables
- Well-defined time horizons and conventions

Explicitly Not Responsible For:
- Deciding whether a metric is “good” or “bad”
- Applying strategy preferences
- Ranking or prioritization

---

### 3. Strategy Logic Module
**Purpose:** Define what it means for a security to *fit* a strategy.

Responsibilities:
- Hard eligibility constraints
- Strategy-specific preferences and tolerances
- Mapping of metrics to qualitative intent
- Buy vs. sell symmetry rules

Outputs:
- Strategy-relative evaluations
- Pass/fail eligibility flags
- Strategy-scoped scores (with full breakdowns)

Explicitly Not Responsible For:
- Creating new metrics
- Comparing across strategies
- Designing outputs or dashboards

---

### 4. Ranking & Decision-Support Module
**Purpose:** Prioritize analyst attention.

Responsibilities:
- Ranking mechanics
- Tiering (e.g., Review / Watch / Ignore)
- Change detection (e.g., rank deterioration)
- Explanation scaffolding

Outputs:
- Ordered candidate lists
- Sell/monitor flags
- Explicit rationales for ranking position

Explicitly Not Responsible For:
- Declaring recommendations
- Optimizing portfolios
- Automating decisions

---

### 5. Output & UX Module
**Purpose:** Present information in a form humans can reason about.

Responsibilities:
- Tables, charts, and summaries
- One-page research dossiers
- Consistent output formats
- Alert and monitoring views

Outputs:
- Human-readable artifacts
- Advisor-friendly comparisons

Explicitly Not Responsible For:
- Modifying logic
- Introducing new signals
- Re-interpreting metrics

---

## Interface Boundaries

All inter-module communication occurs through explicit interfaces:

1. Data → Metrics  
2. Metrics → Strategy Logic  
3. Strategy Logic → Ranking  
4. Ranking → Outputs  

Each interface must be documented in `docs/interfaces/` with:
- Required inputs
- Defined outputs
- Assumptions
- Non-responsibilities

No module may depend on undocumented internal details of another.

---

## AI Integration Boundary (Future)

AI tools, if introduced later:
- May consume outputs from any module
- May summarize, narrate, or highlight anomalies
- May NOT generate new metrics, scores, rankings, or signals

AI is an interpretive layer only, never an analytical authority.

---

## Architectural Invariants

The following principles are non-negotiable:
- Deterministic logic
- Explainability at every stage
- Strategy-relative (not absolute) evaluation
- Human judgment remains explicit

Violations of these invariants require architectural review.