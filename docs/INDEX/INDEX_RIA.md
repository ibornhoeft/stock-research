##### File Index — Research Ingestion Assistant (RIA)

##### docs/INDEX/INDEX_RIA.md
- this file
- owned and maintained by RIA

##### docs/TODO/TODO_RIA.md
- ingestion pipeline tracking

##### docs/01A_Research_Ingestion_Module.md
- defines responsibilities and scope

##### research_ingestion/
- all PDF parsing and NLP logic

##### research_ingestion/testing/
- test harness + validation tooling

---

## Architecture Summary

RIA transforms unstructured PDFs into structured signals:

PDF → Text → Structure → Signals → Validation → Entities → Attribution → Structured Output

---

## Current System State

### ✅ Phase 1 — Complete
- PDF extraction
- basic parsing
- keyword-based signals

### ✅ Phase 2 — Complete
- entity resolution
- noise filtering
- attribution
- aggregation layer (foundational)

### ✅ Phase 3 — Complete
- structure-aware parsing
- sentence-level signal extraction
- signal validation + deduplication
- attribution confidence

---

## Current Capabilities

- deterministic PDF ingestion
- entity extraction + validation
- clean signal extraction (thesis / risks / catalysts)
- sentiment tagging
- traceability to source
- multi-document aggregation (basic)
- test harness for validation

---

## Cross-Module Dependencies

RIA feeds:
- Metrics (optional)
- Strategy (indirect)
- Ranking (indirect)

RIA must NOT:
- perform quantitative scoring
- make investment decisions
- implement ranking logic

---

## Design Constraints

- Traceability to source PDFs
- Deterministic parsing preferred
- AI limited to tagging/summarization
- Modular architecture
- Testability required before expansion