from fastapi import UploadFile
from PyPDF2 import PdfReader

# extracts the text
def extracttxt(file: UploadFile) -> str:
    filename = file.filename.lower()

    if filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

    elif filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    else:
        raise ValueError("Unsupported file type")
