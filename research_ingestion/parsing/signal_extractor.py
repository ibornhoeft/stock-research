import re

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

            if len(s) < 40:  # remove noise
                continue

            section_lower = section.lower()

            if "thesis" in section_lower or "view" in section_lower:
                signals["thesis"].append(s)

            elif "risk" in section_lower:
                signals["risks"].append(s)

            elif "catalyst" in section_lower or "driver" in section_lower:
                signals["catalysts"].append(s)

    return signals