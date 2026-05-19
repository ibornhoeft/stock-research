import uuid

from research_ingestion.extraction.pdf_extractor import extract_pdf_text
from research_ingestion.parsing.section_parser import parse_sections
from research_ingestion.entity.entity_extractor import extract_tickers
from research_ingestion.signals.sentiment_tagger import classify_sentiment, extract_themes
from schema import DocumentOutput, Entity, Sentiment, Traceability

from research_ingestion.entity.entity_resolver import load_ticker_map, resolve_entities
from research_ingestion.entity.cleaner import filter_noise
from research_ingestion.parsing.attribution import split_paragraphs, attribute_paragraphs


def process_pdf(file_path, ticker_map_path):
    document_id = str(uuid.uuid4())

    # -------------------
    # STEP 1: Extract
    # -------------------
    pages = extract_pdf_text(file_path)
    full_text = " ".join([p["text"] for p in pages])

    # -------------------
    # STEP 2: Sections
    # -------------------
    sections, page_map = parse_sections(pages)

    # -------------------
    # STEP 3: Raw Entities
    # -------------------
    raw_entities = extract_tickers(pages)

    # -------------------
    # STEP 4: Clean + Resolve
    # -------------------
    cleaned_entities = filter_noise(raw_entities)

    ticker_map = load_ticker_map(ticker_map_path)
    resolved_entities = resolve_entities(cleaned_entities, ticker_map)

    # Convert to schema objects
    entities = [
        Entity(
            company_name=e["company_name"],
            ticker_candidates=[e["ticker"]],
            mention_count=e["mention_count"]
        )
        for e in resolved_entities
    ]

    # -------------------
    # STEP 5: Attribution
    # -------------------
    paragraphs = split_paragraphs(pages)
    tickers = [e["ticker"] for e in resolved_entities]

    attribution = attribute_paragraphs(paragraphs, tickers)

    # -------------------
    # STEP 6: Sentiment
    # -------------------
    section_sentiment = {}
    for sec, content in sections.items():
        section_text = " ".join(content)
        if section_text:
            section_sentiment[sec] = classify_sentiment(section_text)

    overall_sentiment = classify_sentiment(full_text)

    sentiment = Sentiment(
        overall=overall_sentiment,
        by_section=section_sentiment
    )

    # -------------------
    # STEP 7: Themes
    # -------------------
    themes = extract_themes(full_text)

    # -------------------
    # STEP 8: Signals
    # -------------------
    signals = {
        "thesis": sections["thesis"],
        "risks": sections["risks"],
        "catalysts": sections["catalysts"]
    }

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

    # Attach attribution (non-schema extension, acceptable)
    document.attribution = attribution

    return document