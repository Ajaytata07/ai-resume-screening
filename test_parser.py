from utils.parser import extract_text_from_pdf

file_path = "sample.pdf"

with open(file_path, "rb") as f:
    text = extract_text_from_pdf(f)

print(text)
