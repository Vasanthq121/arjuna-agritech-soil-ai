from pathlib import Path

from app.parser.pdf_reader import PDFReader


class DocumentRouter:

    @staticmethod
    def extract(file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension != ".pdf":
            raise ValueError(
                "Version 1 supports only PDF reports."
            )

        return PDFReader.extract_text(file_path)