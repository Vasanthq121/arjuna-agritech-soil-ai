from app.parser.pdf_reader import PDFReader
from app.llm.extractor import SoilExtractor
from app.normalization.normalizer import SoilNormalizer
from app.validation.validator import SoilValidator
from app.recommendation.recommendation_engine import RecommendationEngine


class SoilAnalysisService:

    @staticmethod
    def analyze(pdf_path: str, crop: str):

        # Read PDF
        text = PDFReader.extract_text(pdf_path)

        # Extract structured data
        raw = SoilExtractor.extract(text)

        # Normalize
        normalized = SoilNormalizer.normalize(raw)

        # Validate
        report = SoilValidator.validate(normalized)

        # Recommendation
        recommendations = RecommendationEngine.generate(
            report=report,
            crop=crop
        )

        return {
            "report": report,
            "recommendations": recommendations
        }