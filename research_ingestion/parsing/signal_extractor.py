import re

from research_ingestion.validation.signal_validator import validate_signals

SENTENCE_SPLIT = r'(?<=[.!?]) +'


def extract_signals(blocks):
    signals = {
        "thesis": [],
        "risks": [],
        "catalysts": []
    }

    for block in blocks:
        section = block["section"]
        sentences = re.split(SENTENCE_SPLIT, block["text"])

        for sentence in sentences:
            s = sentence.strip()

            if len(s.split()) < 6:  # remove noise
                continue

            if not is_meaningful_sentence(s):
                continue

            section_lower = section.lower()

            if "thesis" in section_lower or "view" in section_lower:
                signals["thesis"].append(clean_sentence(s))

            elif "risk" in section_lower:
                signals["risks"].append(clean_sentence(s))

            elif "catalyst" in section_lower or "driver" in section_lower:
                signals["catalysts"].append(clean_sentence(s))

    # ✅ FALLBACK: if no signals found, extract from entire document
    if not any(signals.values()):
        sentences = re.split(SENTENCE_SPLIT, " ".join([b["text"] for b in blocks]))

        for s in sentences:
            s = s.strip()

            if len(s.split()) < 6:
                continue

            # simple heuristic fallback
            if "growth" in s.lower() or "beat" in s.lower():
                signals["thesis"].append(clean_sentence(s))
            elif "risk" in s.lower() or "pressure" in s.lower():
                signals["risks"].append(clean_sentence(s))
            elif "expect" in s.lower() or "outlook" in s.lower():
                signals["catalysts"].append(clean_sentence(s))

    signals = validate_signals(signals)
    signals = dedupe(signals)

    return signals

def is_meaningful_sentence(s):
    s_lower = s.lower()

    important_words = [
        "believe",
        "expect",
        "driven",
        "growth",
        "risk",
        "pressure",
        "outlook",
        "demand",
        "trend",
        "beat",
        "miss",
        "reiterate",
        "stupid",
        "cheap",
        "stupid cheap"
    ]

    return any(w in s_lower for w in important_words)

def clean_sentence(s):
    # remove excessive whitespace
    s = " ".join(s.split())

    # truncate overly long sentences
    if len(s) > 300:
        s = s[:300] + "..."

    return s

def dedupe(signals):
    out = {}
    for k, lst in signals.items():
        seen = set()
        clean = []

        for s in lst:
            key = s.lower()
            if key not in seen:
                clean.append(s)
                seen.add(key)

        out[k] = clean
    return out