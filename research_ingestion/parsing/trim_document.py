def truncate_at_disclaimer(text):
    cutoff_phrases = [
        "important investor disclosures",
        "analyst compensation",
        "regulatory disclosures",
        "page 3 of",
        "page 4 of"
    ]

    text_lower = text.lower()

    for phrase in cutoff_phrases:
        idx = text_lower.find(phrase)
        if idx != -1:
            return text[:idx]

    return text