STOPWORDS = {
    "EPS", "CEO", "CFO", "EBITDA", "USD", "FY", "Q1", "Q2", "Q3", "Q4"
}

def filter_noise(entities):
    cleaned = []

    for e in entities:
        ticker = e["ticker_candidates"][0]

        if ticker not in STOPWORDS:
            cleaned.append(e)

    return cleaned