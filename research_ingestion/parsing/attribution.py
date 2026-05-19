def split_paragraphs(pages):
    paragraphs = []

    for page in pages:
        parts = page["text"].split("\n\n")

        for p in parts:
            paragraphs.append({
                "text": p,
                "page": page["page_number"]
            })

    return paragraphs

def attribute_paragraphs(paragraphs, tickers):
    entity_map = {t: [] for t in tickers}

    for p in paragraphs:
        text = p["text"]

        for ticker in tickers:
            if ticker in text:
                entity_map[ticker].append(p)

    return entity_map