import csv

def load_ticker_map(file_path):
    ticker_map = {}

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ticker_map[row["ticker"]] = row["company_name"]

    return ticker_map

def resolve_entities(raw_entities, ticker_map, full_text):
    resolved = []
    fallback = []

    for entity in raw_entities:
        ticker = entity["ticker_candidates"][0]

        # ✅ PRIMARY: strict match to known ticker map
        if ticker in ticker_map:
            resolved.append({
                "company_name": ticker_map[ticker],
                "ticker": ticker,
                "mention_count": entity["mention_count"]
            })

        # ✅ SECONDARY: collect fallback candidates
        elif entity["mention_count"] >= 3:
            fallback.append({
                "company_name": "UNKNOWN",
                "ticker": ticker,
                "mention_count": entity["mention_count"]
            })

    # ✅ FAILSAFE: if nothing resolved, allow fallback
    if not resolved and fallback:
        fallback_sorted = sorted(
            fallback,
            key=lambda x: x["mention_count"],
            reverse=True
        )

        # Keep top few candidates
        resolved = fallback_sorted[:3]

    text = full_text.upper()

    filtered_resolved = []

    
    for e in resolved:
        if appears_in_context(text, e["ticker"]):
            filtered_resolved.append(e)

    if filtered_resolved:
        return filtered_resolved

    return resolved

# ✅ Only keep tickers appearing near company name patterns
def appears_in_context(text, ticker):
    return (
        f"({ticker})" in text or
        f"{ticker}-" in text or
        f" {ticker} " in text
    )