## AI_CHAT_HANDOFF — Research Ingestion Assistant (RIA)

### Current Responsibilities

This module is responsible for:
- PDF ingestion
- text extraction
- signal extraction (thesis, risks, catalysts)
- entity identification
- sentiment tagging
- attribution
- aggregation

STRICTLY does NOT:
- rank securities
- apply strategy logic
- generate investment recommendations

---

## Current System State

### ✅ Phase 1 — Complete
- PDF text extraction
- keyword section parsing
- ticker regex extraction

### ✅ Phase 2 — Complete
- entity resolution (ticker → company)
- noise filtering
- paragraph-level attribution
- aggregation (basic)

### ✅ Phase 3 — Complete
- structure-aware parsing
- sentence-level signal extraction
- signal validation
- attribution confidence

### ✅ Phase 4 — Implemented (But Failing In Validation)
- layout-aware parsing (coordinates)
- column-aware reconstruction
- improved line grouping

---

## Current Pipeline

PDF  
→ layout extraction  
→ column detection  
→ line reconstruction  
→ structure parsing  
→ signal extraction  
→ signal validation  
→ entity resolution  
→ attribution (+ confidence)  
→ sentiment + themes  
→ structured output  

---

## New Additions (This Phase)

### 🧪 Test Harness
- inspection tooling for pipeline outputs
- structured debugging views (signals, entities, attribution)

### 📄 Synthetic Test Cases
- clean report
- multi-company report
- noisy report
- malformed structure report

### 📊 Real PDF Testing Capability
- directory structure for real reports
- repeatable execution via sample_runner.py

---

## Key Design Constraints

- deterministic first
- explainable outputs
- full traceability to source PDFs
- modular and inspectable pipeline
- no scoring or ranking logic

---

## Known Weaknesses

### High Priority
- section misclassification (varied report formats)
- ticker ambiguity
- attribution misses implicit references

### Medium Priority
- redundant signals
- overly verbose extraction
- theme inconsistency

---

## Active Work

- validating Phase 4 layout parsing
- testing across real PDF reports
- debugging signal extraction quality
- improving line reconstruction accuracy

---

## Immediate Next Steps

1. Run test harness on:
   - synthetic cases (sanity check)
   - 3–5 real research PDFs

2. Evaluate:
   - signal clarity
   - entity correctness
   - attribution coverage

3. Document:
   - failure cases
   - parsing breakdowns
   - noise issues

---

## Critical Rule

NO new features without:
- test harness validation
- traceability preserved

---

## Restart Recommendation

Trigger a clean restart when:
- layout parsing validation is complete
- additional parsing complexity is introduced
- AI-assisted tagging is added

---

## System Status Summary

The ingestion pipeline is now:

✅ modular  
✅ deterministic  
✅ layout-aware  
✅ testable  
✅ production-capable (pending validation)  

The primary risk has shifted from architecture → **data variability + parsing precision**