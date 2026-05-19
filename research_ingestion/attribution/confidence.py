def compute_confidence(paragraph, ticker):
    text = paragraph["text"]

    count = text.count(ticker)

    if count >= 2:
        return "high"
    elif count == 1:
        return "medium"
    else:
        return "low"


def apply_confidence(attribution):
    output = {}

    for ticker, paragraphs in attribution.items():
        enriched = []

        for p in paragraphs:
            enriched.append({
                "text": p["text"],
                "page": p["page"],
                "confidence": compute_confidence(p, ticker)
            })

        output[ticker] = enriched

    return output