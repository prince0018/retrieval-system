from pypdf import PdfReader
from src.text_splitter import get_recursive_text_splitter


def extract_text_from_pdf(pdf_path: str) -> list[str]:
    reader = PdfReader(pdf_path)
    pages_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)

    return pages_text


def split_text_with_langchain(text: str) -> list[str]:
    splitter = get_recursive_text_splitter()
    return splitter.split_text(text)