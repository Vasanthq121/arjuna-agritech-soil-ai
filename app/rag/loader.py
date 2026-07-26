from pathlib import Path
from pypdf import PdfReader
from docx import Document


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md", ".docx"}


def load_pdf(path: Path) -> str:
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def load_docx(path: Path) -> str:
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_document(path: Path) -> str:
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return load_pdf(path)

    if suffix == ".docx":
        return load_docx(path)

    if suffix in [".txt", ".md"]:
        return load_text(path)

    raise ValueError(f"Unsupported file type: {suffix}")


def load_folder(folder: str):
    folder = Path(folder)

    docs = []

    for file in folder.rglob("*"):
        if file.suffix.lower() in SUPPORTED_EXTENSIONS:
            docs.append(
                {
                    "source": str(file),
                    "text": load_document(file),
                }
            )

    return docs