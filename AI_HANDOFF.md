# AI_HANDOFF.md

# Chat Continuity Guide

## Purpose of This Document

This document defines how a human operator can **restart any AI role**
with **zero prior chat history** while preserving full project continuity.

It exists to make all AI roles **explicit, scoped, and replaceable at any time**
without loss of architectural intent, authority boundaries, or institutional memory.

This document does NOT define system semantics.
Those are defined in the uploaded documentation.

---

## Conversation Continuity Rule (All Roles)

AI roles must actively monitor **accumulated conversational context and task scope**.

If the conversation grows to a point where losing context would meaningfully
disrupt continuity, the AI **must warn the operator several turns in advance**
and propose a handoff plan.

A handoff warning should include:
- what context or decisions must be preserved
- which documents or notes should be transferred
- whether the current task should be paused or wrapped up before restarting

AI roles must **not wait until a hard limit or forced termination** to raise
continuity concerns.

Continuity is a first‑class responsibility.

---

## General Restart Procedure (All Roles)

1. Create a new AI chat with no prior context
2. Upload the required documents listed for the role
3. Use the provided restart prompt verbatim
4. The AI MUST treat uploaded documentation as authoritative
5. The AI MUST NOT assume undocumented intent
6. If documentation is unclear, updating documentation comes before changing code

---

## Project Summary
Internal research assistant system for stock and fund analysis.
AI-free core. Deterministic, explainable, modular design.

## Current Phase
Phase 2 complete. Transitioning to Phase 3 (Initial Implementation).

## Canonical Documents
- docs/00_Canonical_Vision.md (authoritative)
- docs/interfaces/ (module contracts)

## Open Decisions
- First stock strategy to formalize
- Universe data source finalization

## Recently Completed
- Python environment set up using Miniforge
- Project skeleton created
- Multi-chat architecture defined
- Canonical vision locked
- System architecture finalized
- Interface philosophy defined
- Phase 2 module documentation completed

## Next Intended Actions
- Implement Metrics module in Python
- Implement Core Quality Growth strategy
- Run end-to-end on toy universe

## Governance Rules
- No AI decision-making logic
- All cross-module logic must respect interface contracts
- Documentation precedes code