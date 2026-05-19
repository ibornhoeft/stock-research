import re

def is_header(line):
    if not line.strip():
        return False

    # Heuristics:
    return (
        line.isupper() or
        len(line.split()) <= 6 and line.endswith(":")
    )


def parse_document_structure(pages):
    blocks = []

    current_section = "unknown"
    current_text = []

    for page in pages:
        for line in page["text"].split("\n"):

            if is_header(line):
                if current_text:
                    blocks.append({
                        "section": current_section,
                        "text": " ".join(current_text),
                        "page": page["page_number"]
                    })
                    current_text = []

                current_section = line.lower()

            else:
                current_text.append(line)

    return blocks