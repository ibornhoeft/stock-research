# Research Ingestion & Parsing Module

## Purpose

Transform unstructured research report PDFs into structured, queryable data
that can be used to prioritize securities for analyst review.

This module is the primary entry point for qualitative information.

---

## Inputs

- Sell-side research PDFs (FactSet downloads)
- Fund reports and commentaries

---

## Outputs

Structured data including:
- Tickers mentioned
- Sentiment indicators (positive, negative, cautious)
- Key themes (growth, risks, catalysts)
- Recommendation strength (if present)
- Frequency of mention across reports

---

## Responsibilities

- Extract text from PDFs
- Identify companies / tickers
- Classify sections (thesis, risks, valuation)
- Tag key phrases and themes
- Aggregate signals across reports

---

## Explicitly Not Responsible For

- Quantitative metric calculation
- Portfolio decisions
- Strategy evaluation

---

## Design Principles

- Deterministic where possible
- AI (optional) used only for tagging/summarization
- Full traceability back to source PDFs

---

## Output Goal

A ranked list of securities based on:
- Frequency of coverage
- Strength of positive/negative language
- Presence of catalysts or warnings