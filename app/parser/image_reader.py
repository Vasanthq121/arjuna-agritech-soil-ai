from app.parser.paddle_ocr import OCRReader


class ImageReader:

    @staticmethod
    def extract_text(file_path: str) -> str:
        return OCRReader.extract_text(file_path)