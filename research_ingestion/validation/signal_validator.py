
def is_valid_signal(text):
    text_lower = text.lower()

    # ❌ reject emails / contacts
    if "@" in text:
        return False

    # reject tables
    if is_table_like(text):
        return False

    # reject labels
    if is_label_block(text):
        return False

    # ❌ reject numeric-heavy lines (tables)
    digit_ratio = sum(c.isdigit() for c in text) / max(len(text), 1)
    if digit_ratio > 0.25:
        return False

    # ❌ reject boilerplate keywords
    bad_phrases = [
        "all rights reserved",
        "page",
        "analyst compensation",
    ]

    if any(p in text_lower for p in bad_phrases):
        return False

    # MUST contain real analyst language
    strong_words = [
        "expect", "believe", "driven", "growth",
        "pressure", "trend", "outlook", "beat",
        "miss", "reiterate"
    ]

    if not any(w in text_lower for w in strong_words):
        return False

    return True

def validate_signals(signals):
    validated = {}

    for k, items in signals.items():
        filtered = []

        seen = set()

        for s in items:
            if not is_valid_signal(s):
                continue

            key = s.strip().lower()

            if key not in seen:
                filtered.append(s)
                seen.add(key)

        validated[k] = filtered

    return validated

def is_table_like(text):
    digit_ratio = sum(c.isdigit() for c in text) / max(len(text), 1)

    # higher threshold → less aggressive
    if digit_ratio > 0.30:
        return True

    # reject dense numeric/token mix
    tokens = text.split()
    if len(tokens) > 15:
        numeric_tokens = sum(1 for t in tokens if any(c.isdigit() for c in t))
        if numeric_tokens / len(tokens) > 0.4:
            return True

    return False

def is_label_block(text):
    words = text.split()

    if len(words) < 10 and text.isupper():
        return True

    if text.endswith(":"):
        return True

    return False