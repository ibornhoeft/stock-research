## Metric Glossary

This document defines all quantitative metrics produced by the **Metrics & Diagnostics** module. All definitions are deterministic, numerically explicit, and interface-compliant with **Data → Metrics** and **Metrics → Strategy Logic**.

---

### Returns

- **Daily Log Return**:  
  \( r_t = \ln(P_t / P_{t-1}) \), using adjusted close prices.  
  Assumes prices are split- and dividend-adjusted upstream.

- **Rolling Cumulative Log Return (window \(W\))**:  
  \( R_{t,W} = \sum_{i=0}^{W-1} r_{t-i} \)

---

### Risk Metrics

- **Volatility (annualized)**:  
  \( \sigma_{ann} = \sqrt{252} \cdot \operatorname{std}(r_t) \), computed over an explicit rolling window.

- **Maximum Drawdown**:  
  Based on cumulative return path \( C_t = \exp(\sum r_t) \):  
  \( \max_{t} \left( \frac{C_t - \max_{s \le t} C_s}{\max_{s \le t} C_s} \right) \)

- **Beta vs. Benchmark**:  
  \( \beta = \frac{\operatorname{cov}(r_{asset}, r_{bench})}{\operatorname{var}(r_{bench})} \), using synchronous returns and identical windows.

---

### Valuation Metrics

- **Trailing Multiples** (e.g., P/E, EV/EBITDA):  
  Point-in-time fundamental denominator divided into contemporaneous price or enterprise value.

- **Historical Percentile**:  
  Empirical percentile of the current multiple relative to its own historical distribution over a defined lookback window.

---

### Factor Metrics

- **Momentum**:  
  Rolling cumulative return over window \(W\), excluding the most recent \(k\) days (both parameters explicit).

- **Value Proxies**:  
  Inverted valuation multiples expressed as normalized numerical series.

- **Quality Proxies**:  
  Deterministic transformations of profitability and balance-sheet fields (definitions enumerated per metric).

---

### Conventions

- All rolling windows are explicitly parameterized and named.
- No silent imputation: missing observations propagate with flags.
- All metrics are computed cross-sectionally independent.
- Units, scaling, and sign conventions are fixed at definition time.

---

## AI_CHAT_HANDOFF — Metrics & Diagnostics

**Scope:** Quantitative definition, computation, and validation of observable security properties.

**Last updated:** 2026-04-22

### Completed

- Data → Metrics interface acknowledged and enforced
- Deterministic return, risk, valuation, and factor metric families defined
- Explicit mathematical formulations documented
- Missing-data propagation conventions formalized
- Point-in-time and survivorship assumptions documented (upstream-dependent)

### Explicit Non-Responsibilities

- No strategy preferences, thresholds, or scoring logic
- No ranking, prioritization, or qualitative interpretation
- No output or visualization design

### Open Items

- Formal factor model enumeration (set membership only, no weighting)
- Cross-metric correlation diagnostics specification
- Numerical stability checks for thin-history securities

### Next Actions (Metrics Module only)

- Encode all definitions in Metrics module with parameterized windows
- Produce validation diagnostics (self-consistency, NaN coverage)
- Expose metric histories and snapshots per Metrics → Strategy interface

**Invariant:** Metric definitions are frozen prior to any Strategy Logic application.