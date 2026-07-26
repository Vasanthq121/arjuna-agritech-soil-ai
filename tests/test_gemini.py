from pathlib import Path
from pprint import pprint

from app.parser.document_router import DocumentRouter
from app.llm.extractor import SoilExtractor

# Always resolve from the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
UPLOAD_DIR = PROJECT_ROOT / "uploads" / "original"

print("Project Root :", PROJECT_ROOT)
print("Upload Folder:", UPLOAD_DIR)

pdfs = list(UPLOAD_DIR.glob("*.pdf"))

print("PDFs Found:", len(pdfs))
print(pdfs)

if not pdfs:
    raise FileNotFoundError(f"No PDF files found in {UPLOAD_DIR}")

latest = max(pdfs, key=lambda p: p.stat().st_mtime)

print("Reading:", latest.name)

text = DocumentRouter.extract(str(latest))

data = SoilExtractor.extract(text)

pprint(data)