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