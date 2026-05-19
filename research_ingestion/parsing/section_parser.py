SECTION_KEYWORDS = {
    "thesis": [
        "company brief",
        "overview",
        "analysis",
        "summary"
    ],
    "risks": [
        "risk",
        "risk factors",
        "company specific risk"
    ],
    "catalysts": [
        "catalyst",
        "drivers"
    ],
}

def parse_sections(pages):
    sections = {k: [] for k in SECTION_KEYWORDS}
    page_map = {k: [] for k in SECTION_KEYWORDS}

    for page in pages:
        lines = page["text"].split("\n")
        current_section = None

        for line in lines:
            line_lower = line.lower()

            # Detect headers (simple heuristic)
            if line.isupper() and len(line.split()) < 8:
                current_section = None

            for section, keywords in SECTION_KEYWORDS.items():
                if any(k in line_lower for k in keywords):
                    current_section = section

            if current_section:
                sections[current_section].append(line)
                page_map[current_section].append(page["page_number"])

    return sections, page_map