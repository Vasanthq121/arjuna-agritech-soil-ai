from pathlib import Path
from uuid import uuid4

ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg"}


def generate_report_id() -> str:
    return str(uuid4())


def get_extension(filename: str) -> str:
    return Path(filename).suffix.lower()


def is_allowed(filename: str) -> bool:
    return get_extension(filename) in ALLOWED_EXTENSIONS