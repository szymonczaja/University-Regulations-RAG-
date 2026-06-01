from pypdf import PdfReader

def extract_text_from_pdf(file_path:str) -> str:
    text = ""
    reader = PdfReader(file_path)
    for x in reader.pages:
        t = x.extract_text()
        text += t if t is not None else ""
    return text      