from pathlib import Path

from app.database.crud import save_report
from app.database.database import SessionLocal
from app.llm.extractor import SoilExtractor
from app.normalization.normalizer import SoilNormalizer
from app.parser.document_router import DocumentRouter
from app.validation.validator import SoilValidator

PROJECT_ROOT = Path(__file__).resolve().parent.parent
UPLOAD_DIR = PROJECT_ROOT / "uploads" / "original"

latest = max(
    UPLOAD_DIR.glob("*.pdf"),
    key=lambda p: p.stat().st_mtime
)

text = DocumentRouter.extract(str(latest))

raw = SoilExtractor.extract(text)

normalized = SoilNormalizer.normalize(raw)

validated = SoilValidator.validate(normalized)

db = SessionLocal()

report = save_report(
    db,
    validated.model_dump()
)

print(report.id)
print(report.sample_id)