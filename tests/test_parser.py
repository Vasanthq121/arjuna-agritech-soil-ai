from pathlib import Path

from app.parser.document_router import DocumentRouter

UPLOAD_DIR = Path("uploads/original")

pdfs = list(UPLOAD_DIR.glob("*.pdf"))

if not pdfs:
    raise Exception("No PDF uploaded.")

latest = max(
    pdfs,
    key=lambda x: x.stat().st_mtime
)

print("=" * 80)
print("Reading:", latest.name)
print("=" * 80)

text = DocumentRouter.extract(str(latest))

print(text[:5000])

print("\n")
print("=" * 80)
print("Characters:", len(text))
print("=" * 80)