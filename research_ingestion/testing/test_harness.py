import json


def print_section(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")


def inspect_pages(pages):
    print_section("RAW EXTRACTION")
    for p in pages[:2]:  # limit output
        print(f"[Page {p['page_number']}]: {p['text'][:500]}")


def inspect_entities(entities):
    print_section("ENTITIES")
    for e in entities:
        print(e)


def inspect_signals(signals):
    print_section("SIGNALS")
    for k, v in signals.items():
        print(f"{k.upper()}:")
        for s in v[:3]:
            print(f" - {s}")


def inspect_sentiment(sentiment):
    print_section("SENTIMENT")
    print(sentiment)


def inspect_attribution(attribution):
    print_section("ATTRIBUTION")
    for ticker, items in attribution.items():
        print(f"{ticker}: {len(items)} paragraphs")
        for p in items[:2]:
            print(f"  [{p['confidence']}] {p['text'][:150]}")


def inspect_document(doc):
    print_section("FINAL DOCUMENT SUMMARY")
    print(f"File: {doc.file_name}")
    print(f"Entities: {len(doc.entities)}")
    print(f"Themes: {doc.themes}")