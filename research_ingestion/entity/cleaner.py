STOPWORDS = {
    # common junk tokens
    "THE", "AND", "FOR", "WITH", "FROM", "THIS", "THAT", "PAGE", "OF",

    # finance terms
    "EPS", "CEO", "CFO", "EBITDA", "GAAP", "USD", "FY", "Q1", "Q2", "Q3", "Q4",

    # company suffixes
    "INC", "CORP", "LTD", "GROUP", "PLC", "CO", "LLC"
}

def filter_noise(entities):
    cleaned = []

    for e in entities:
        ticker = e["ticker_candidates"][0]

        if ticker not in STOPWORDS:
            cleaned.append(e)

    return cleaned