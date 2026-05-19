import pdfplumber

def extract_pdf_text(file_path):
    pages = []

    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""

            pages.append({
                "page_number": i + 1,
                "text": text
            })

    return pages

def extract_with_layout(file_path):
    import pdfplumber

    structured_pages = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words()

            structured_pages.append({
                "page_number": page.page_number,
                "words": words
            })

    return structured_pages

def extract_layout(file_path):
    import pdfplumber

    pages = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words()

            pages.append({
                "page_number": page.page_number,
                "words": words,
                "width": page.width
            })

    return pages