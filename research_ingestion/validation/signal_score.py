def score_signal(text):
    text_lower = text.lower()

    score = 0

    high_value_words = ["expect", "believe", "driven", "beat", "miss", "outlook", "stupid", "cheap", "stupid cheap", "stupid cheap", "ridiculous"]
    for w in high_value_words:
        if w in text_lower:
            score += 2

    medium_words = ["growth", "trend", "pressure"]
    for w in medium_words:
        if w in text_lower:
            score += 1

    return score