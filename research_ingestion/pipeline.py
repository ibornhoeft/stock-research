import uuid

from research_ingestion.extraction.pdf_extractor import extract_pdf_text
from research_ingestion.parsing.section_parser import parse_sections
from research_ingestion.entity.entity_extractor import extract_tickers
from research_ingestion.signals.sentiment_tagger import classify_sentiment, extract_themes
from schema import DocumentOutput, Entity, Sentiment, Traceability

from research_ingestion.entity.entity_resolver import load_ticker_map, resolve_entities
from research_ingestion.entity.cleaner import filter_noise

from parsing.structure_parser import parse_document_structure
from parsing.signal_extractor import extract_signals
from validation.signal_validator import validate_signals
from attribution.attribution import split_paragraphs, attribute_paragraphs
from attribution.confidence import apply_confidence

def process_pdf(file_path, ticker_map_path):
    document_id = str(uuid.uuid4())

    # -------------------
    # STEP 1: Extract
    # -------------------
    pages = extract_pdf_text(file_path)
    full_text = " ".join([p["text"] for p in pages])

    # -------------------
    # STEP 2: Structure Parsing (NEW)
    # -------------------
    blocks = parse_document_structure(pages)

    # -------------------
    # STEP 3: Signals (NEW)
    # -------------------
    raw_signals = extract_signals(blocks)
    signals = validate_signals(raw_signals)

    # -------------------
    # STEP 4: Legacy Section Mapping (for compatibility)
    # -------------------
    sections, page_map = parse_sections(pages)

    # -------------------
    # STEP 5: Entities
    # -------------------
    raw_entities = extract_tickers(pages)
    cleaned_entities = filter_noise(raw_entities)

    ticker_map = load_ticker_map(ticker_map_path)
    resolved_entities = resolve_entities(cleaned_entities, ticker_map)

    entities = [
        Entity(
            company_name=e["company_name"],
            ticker_candidates=[e["ticker"]],
            mention_count=e["mention_count"]
        )
        for e in resolved_entities
    ]

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