from app.parser.pdf_reader import PDFReader
from app.llm.extractor import SoilExtractor
from app.normalization.normalizer import SoilNormalizer
from app.validation.validator import SoilValidator
from app.recommendation.recommendation_engine import RecommendationEngine
from app.reports.report_generator import ReportGenerator


def main():

    crop = "Rice"

    pdf_path = "knowledge_base/soil_health_card/example_soil_testing_report.pdf"

    text = PDFReader.extract_text(pdf_path)

    raw = SoilExtractor.extract(text)

    normalized = SoilNormalizer.normalize(raw)

    report = SoilValidator.validate(normalized)

    recommendations = RecommendationEngine.generate(
        report,
        crop
    )

    ReportGenerator.generate(
        report,
        recommendations,
        "soil_recommendation_report.pdf"
    )

    print("PDF generated successfully!")


if __name__ == "__main__":
    main()