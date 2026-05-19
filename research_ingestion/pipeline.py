import uuid
import os

from research_ingestion.extraction.pdf_extractor import extract_pdf_text
from research_ingestion.parsing.section_parser import parse_sections
from research_ingestion.entity.entity_extractor import extract_tickers
from research_ingestion.parsing.trim_document import truncate_at_disclaimer
from research_ingestion.signals.sentiment_tagger import classify_sentiment, extract_themes
from research_ingestion.schema import DocumentOutput, Entity, Sentiment, Traceability

from research_ingestion.entity.entity_resolver import load_ticker_map, resolve_entities
from research_ingestion.entity.cleaner import filter_noise

from research_ingestion.parsing.structure_parser import parse_document_structure
from research_ingestion.parsing.signal_extractor import extract_signals
from research_ingestion.validation.signal_validator import validate_signals
from research_ingestion.attribution.attribution import split_paragraphs, attribute_paragraphs
from research_ingestion.attribution.confidence import apply_confidence

from research_ingestion.parsing.layout_parser import (
    group_words_into_lines,
    build_text_lines,
    detect_columns
)
from research_ingestion.extraction.pdf_extractor import extract_layout
from research_ingestion.validation.signal_score import score_signal

def process_pdf(file_path, ticker_map_path):
    document_id = str(uuid.uuid4())

    # -------------------
    # STEP 1: Extract
    # -------------------

    layout_pages = extract_layout(file_path)

    pages = []

    for p in layout_pages:
        words = p["words"]

        left, right = detect_columns(words, p["width"])

        lines_left = build_text_lines(group_words_into_lines(left))
        lines_right = build_text_lines(group_words_into_lines(right))

        # interleave lines instead of stacking columns
        text_lines = []

        max_len = max(len(lines_left), len(lines_right))

        for i in range(max_len):
            if i < len(lines_left):
                text_lines.append(lines_left[i])
            if i < len(lines_right):
                text_lines.append(lines_right[i])

        text = "\n".join(text_lines)

        pages.append({
            "page_number": p["page_number"],
            "text": text
        })

    full_text = " ".join([p["text"] for p in pages])

    try:
        debug_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ".",
                "testing",
                "outputs",
                "debug_text.txt"
            )
        )

        os.makedirs(os.path.dirname(debug_path), exist_ok=True)

        with open(debug_path, "w", encoding="utf-8") as f:
            f.write(full_text)

    except Exception as e:
        print("⚠ Debug write failed:", e)

    # -------------------
    # STEP 2: Structure Parsing (NEW)
    # -------------------
    full_text = truncate_at_disclaimer(full_text)
    blocks = parse_document_structure(pages)

    try:
        debug_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ".",
                "testing",
                "outputs",
                "trimmed_text.txt"
            )
        )

        os.makedirs(os.path.dirname(debug_path), exist_ok=True)

        with open(debug_path, "w", encoding="utf-8") as f:
            f.write(full_text)

    except Exception as e:
        print("⚠ Debug write failed:", e)

    # -------------------
    # STEP 3: Signals (NEW)
    # -------------------
    raw_signals = extract_signals(blocks)
    signals = validate_signals(raw_signals)

    def safe_score(signal):
        try:
            return score_signal(signal)
        except Exception:
            return 0

    for k in signals:
        signals[k] = sorted(signals[k], key=safe_score, reverse=True)

    # -------------------
    # STEP 4: Legacy Section Mapping (for compatibility)
    # -------------------
    sections, page_map = parse_sections(pages)

    # -------------------
    # STEP 5: Entities
    # -------------------
    raw_entities = extract_tickers(pages)

    print("RAW TICKERS:", raw_entities[:20])

    cleaned_entities = filter_noise(raw_entities)

    ticker_map = load_ticker_map(ticker_map_path)
    resolved_entities = resolve_entities(cleaned_entities, ticker_map, full_text)

    print("RESOLVED:", resolved_entities)

    entities = [
        Entity(
            company_name=e["company_name"],
            ticker_candidates=[e["ticker"]],
            mention_count=e["mention_count"]
        )
        for e in resolved_entities
    ]

    if not entities:
        print("⚠ WARNING: No entities detected")

    # -------------------
    # STEP 6: Attribution + Confidence
    # -------------------
    paragraphs = split_paragraphs(pages)
    tickers = [e["ticker"] for e in resolved_entities]

    attribution_raw = attribute_paragraphs(paragraphs, tickers)
    attribution = apply_confidence(attribution_raw)

    # -------------------
    # STEP 7: Sentiment
    # -------------------
    section_sentiment = {}
    for sec, content in signals.items():
        combined = " ".join(content)
        if combined:
            section_sentiment[sec] = classify_sentiment(combined)

    overall_sentiment = classify_sentiment(full_text)

    sentiment = Sentiment(
        overall=overall_sentiment,
        by_section=section_sentiment
    )

    # -------------------
    # STEP 8: Themes
    # -------------------
    themes = extract_themes(full_text)

    # -------------------
    # STEP 9: Traceability
    # -------------------
    traceability = Traceability(
        page_map=page_map,
        raw_text_ref=file_path
    )

    # -------------------
    # FINAL OBJECT
    # -------------------
    document = DocumentOutput(
        document_id=document_id,
        file_name=file_path,
        entities=entities,
        signals=signals,
        sentiment=sentiment,
        themes=themes,
        traceability=traceability
    )

    document.attribution = attribution

    return document