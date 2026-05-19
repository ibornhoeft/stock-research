#### File Index — Research Ingestion Assistant (RIA)

#### docs/INDEX/INDEX_RIA.md
- this file
- owned and maintained by RIA

#### docs/TODO/TODO_RIA.md
- ingestion pipeline tracking

#### docs/01A_Research_Ingestion_Module.md
- defines responsibilities and scope

#### research_ingestion/
- all PDF parsing and NLP logic

---

#### Architecture Summary

RIA transforms unstructured PDFs into structured signals:

PDF → Text → Signals → Structured Output

---

#### Cross-Module Dependencies

RIA feeds:
- Metrics (optional)
- Strategy (indirect)
- Ranking (indirect)

RIA must NOT:
- perform quantitative scoring
- make investment decisions
- implement ranking logic

---

#### Design Constraints

- Traceability to source PDFs
- Deterministic parsing preferred
- AI limited to tagging/summarization