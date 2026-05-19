def is_valid_signal(text):
    text = text.lower()

    # Reject boilerplate
    if "copyright" in text or "disclaimer" in text:
        return False

    # Reject numeric dumps
    if sum(c.isdigit() for c in text) > len(text) * 0.3:
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