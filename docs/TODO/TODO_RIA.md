### TODO — Research Ingestion Assistant (RIA)

#### Purpose

Working memory for PDF ingestion pipeline development.

---

## ✅ Completed

### Phase 1
- PDF extraction
- section detection (keyword-based)
- ticker extraction
- basic sentiment tagging

### Phase 2
- entity resolution (ticker → company)
- noise filtering layer
- paragraph-level attribution
- aggregation module (basic)

### Phase 3
- structure-aware parsing
- sentence-level signal extraction
- signal validation + deduplication
- attribution confidence layer

---

## 🧪 Testing (NEW — REQUIRED)

- build test harness ✅
- run pipeline on multiple PDFs ✅
- inspect signal quality ✅
- validate entity correctness ✅

---

## 🚧 Active Work

### 🔍 Signal Quality Refinement
- improve sentence splitting
- reduce redundant signals
- improve readability

### 🧠 Attribution Accuracy
- improve multi-company attribution
- detect implicit references

---

## 🧠 Next Phase (Phase 4)

### 📄 Layout-Aware Parsing
- use PDF coordinates
- detect columns and blocks
- improve section boundary detection

### ✅ Entity Validation (External)
- cross-reference against universe
- eliminate false positives

### 🧪 Confidence Improvements
- refine attribution confidence model
- add signal-level confidence (NOT ranking)

---

## ⚠️ Risks

- inconsistent PDF formatting
- broken layout extraction
- ticker ambiguity
- noisy signals

---

## 🔁 Handoff Reminder

- Always update AI_CHAT_HANDOFF
- Always validate before adding complexity
- Prefer deterministic improvements over AI