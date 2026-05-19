import re
from collections import Counter


def extract_tickers(pages):
    pattern = r'\b[A-Z]{1,5}\b'
    ticker_counter = Counter()

    for page in pages:
        matches = re.findall(pattern, page["text"])
        ticker_counter.update(matches)

    entities = []

    for ticker, count in ticker_counter.items():
        entities.append({
            "company_name": "UNKNOWN",
            "ticker_candidates": [ticker],
            "mention_count": count
        })

    return entities