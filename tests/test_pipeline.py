from pathlib import Path
from pprint import pprint

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

print("\n===== VALIDATED REPORT =====\n")

pprint(validated.model_dump())