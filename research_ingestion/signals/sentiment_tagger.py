SENTIMENT_DICT = {
    "positive": ["strong", "outperform", "buy", "growth", "upside"],
    "negative": ["weak", "underperform", "sell", "decline", "risk"],
    "cautious": ["mixed", "uncertain", "volatile"]
}

THEMES = {
    "growth": ["growth", "expansion"],
    "macro": ["inflation", "rates"],
    "competition": ["competition", "market share"],
    "regulation": ["regulation", "policy"]
}

def classify_sentiment(text):
    text = text.lower()
    scores = {k: 0 for k in SENTIMENT_DICT}

    for sentiment, words in SENTIMENT_DICT.items():
        for word in words:
            if word in text:
                scores[sentiment] += 1

    return max(scores, key=scores.get)

def extract_themes(text):
    text = text.lower()
    found = set()

    for theme, words in THEMES.items():
        for word in words:
            if word in text:
                found.add(theme)

    return list(found)