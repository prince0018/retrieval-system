from src.pdf_utils import extract_text_from_pdf

pdf_path = "sample.pdf"  # put any PDF here

pages = extract_text_from_pdf(pdf_path)

print(f"Total pages extracted: {len(pages)}")
print(pages[0][:500])  # print first 500 characters