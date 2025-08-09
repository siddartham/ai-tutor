import fitz


def extract_pdf(file_path):
    doc = fitz.open(file_path)
    extracted_text = []
    for page in doc:
        text = page.get_text()
        extracted_text.append(text)
    full_document_text = "\n".join(extracted_text)

    return full_document_text
