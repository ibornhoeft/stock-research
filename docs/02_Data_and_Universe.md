## Data and Universe Definitions

This document defines the eligible security universe and the data assumptions
used by the system. It establishes **what can be analyzed**, not **how it is
analyzed**. All downstream modules must treat this document as authoritative.

---

### Initial Scope

The initial investment universe is intentionally constrained to ensure data
quality, interpretability, and auditability.

Included:
- U.S.-listed common equities
- Securities listed on NYSE, NASDAQ, or NYSE American

Explicitly Excluded:
- ADRs and foreign listings
- OTC and pink-sheet securities
- Preferred shares
- Closed-end funds, ETFs, mutual funds
- Warrants, rights, units, SPAC sponsor shares
- Cryptocurrencies and digital assets

Rationale: These exclusions reduce structural heterogeneity and avoid
instrument-specific behaviors that would violate metric comparability or
strategy neutrality.

---

### Inclusion Rules

A security must satisfy **all** of the following at universe construction
(time-of-evaluation):

- Listed on an approved U.S. exchange
- Classified as a common equity (share class explicitly identified)
- Meets minimum market capitalization threshold (configured upstream)
- Meets minimum liquidity threshold (average daily trading volume)
- Has a continuous adjusted price history over the required lookback window

These filters are **structural**, not strategic, and apply uniformly across all
strategies.

---

### Exclusion Rules

Securities are excluded if any of the following apply:

- Incomplete or discontinuous price history that cannot be resolved
- Corporate actions (mergers, spin-offs, symbol re-use) that introduce
  unresolved time-series ambiguity
- Known data integrity issues flagged by the data provider
- Delisted securities **unless** explicitly reintroduced via a
  survivorship-controlled data source

No qualitative or performance-based exclusions are permitted in this module.

---

### Identifier Standards

Each security must be represented by a **stable identifier set**:

Primary Identifier:
- Exchange ticker (string, point-in-time aware)

Secondary Identifiers:
- CUSIP (when available)
- Permanent internal security ID (recommended)

Identifier requirements:
- Identifier mappings must be time-aware (no silent ticker re-use)
- Corporate action events must preserve identity continuity
- Downstream modules may not infer identity from ticker alone

---

### Data Assumptions

The Data & Universe module makes the following explicit assumptions:

- Price series are adjusted for splits and cash dividends
- Fundamental data is point-in-time consistent and appropriately lagged
- Market capitalization is computed using contemporaneous shares outstanding
- Metadata classifications (sector, industry) reflect provider conventions

All assumptions must be documented here before being relied upon downstream.

---

### Data Limitations

Known limitations that downstream modules must respect:

- Survivorship bias depends on data source and must be documented explicitly
- Point-in-time data quality may degrade further back in history
- Corporate action resolution quality varies across issuers and time periods
- Exchange and classification metadata may change retrospectively

No downstream module may silently correct or reinterpret these limitations.

---

### Interface Contract Alignment

This document is the authoritative upstream reference for the
**Data → Metrics** interface.

Downstream expectations:
- Only securities passing this universe may enter Metrics
- Metrics may assume identifiers are standardized and stable
- Metrics must surface missing-data flags, not repair universe gaps

All changes here require a documented review of Metrics assumptions.

---

### Data Source Abstraction

All upstream data sources must be accessed through provider adapters that
convert raw vendor or file-based data into canonical `SecurityRecord` objects.

Approved provider patterns:
- Stub providers (for testing)
- File-based providers (CSV, Parquet)
- Vendor adapters (e.g., FactSet)

Requirements:
- No vendor-specific data structures may propagate beyond the provider layer
- All providers must produce fully-formed `SecurityRecord` objects
- All identifier fields must be mapped explicitly (no implicit inference)

Rationale:
This ensures the universe construction process remains vendor-agnostic,
deterministic, and auditable.

---

## AI_CHAT_HANDOFF — Data & Universe

**Last updated:** 2026-04-22

**Role Scope:**
- Define eligible investment universe
- Specify inclusion and exclusion rules
- Document data assumptions and limitations
- Standardize security identifiers

**Explicit Non-Scope:**
- Metric construction or transformation
- Strategy fit evaluation
- Ranking, scoring, or prioritization

**Completed:**
- Formalized U.S. common equity universe
- Codified structural inclusion and exclusion rules
- Clarified identifier requirements and time-awareness
- Documented data assumptions and known limitations

**Open Questions:**
- Policy for reintroducing delisted securities under survivorship-safe sourcing
- Future international universe expansion (non-U.S. equities)
- Formal ADR handling policy (remain excluded vs. carve-out)

**Next Actions:**
- Sync survivorship-bias treatment with Metrics module documentation
- Validate exchange and security-type classification rules against data vendor
- Confirm minimum liquidity and market-cap configuration ownership