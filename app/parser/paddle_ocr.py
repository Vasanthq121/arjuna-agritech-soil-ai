from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)


class OCRReader:

    @staticmethod
    def extract_text(image_path: str) -> str:

        result = ocr.ocr(image_path)

        lines = []

        for page in result:
            if page is None:
                continue

            for line in page:
                lines.append(line[1][0])

        return "\n".join(lines)