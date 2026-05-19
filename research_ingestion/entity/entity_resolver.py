import csv

def load_ticker_map(file_path):
    ticker_map = {}

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ticker_map[row["ticker"]] = row["company_name"]

    return ticker_map

def resolve_entities(raw_entities, ticker_map):
    resolved = []

    for entity in raw_entities:
        ticker = entity["ticker_candidates"][0]

        if ticker in ticker_map:
            resolved.append({
                "company_name": ticker_map[ticker],
                "ticker": ticker,
                "mention_count": entity["mention_count"]
            })

    return resolved