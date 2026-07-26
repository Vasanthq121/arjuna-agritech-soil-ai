from app.parser.pdf_reader import PDFReader
from app.llm.extractor import SoilExtractor
from app.normalization.normalizer import SoilNormalizer
from app.validation.validator import SoilValidator
from app.recommendation.recommendation_engine import RecommendationEngine


def main():
    crop = "Rice"

    pdf_path = "knowledge_base/soil_health_card/example_soil_testing_report.pdf"

    print("=" * 70)
    print("Reading PDF...")
    text = PDFReader.extract_text(pdf_path)

    print("=" * 70)
    print("Extracting Soil Data...")
    raw = SoilExtractor.extract(text)

    print("=" * 70)
    print("Normalizing...")
    normalized = SoilNormalizer.normalize(raw)

    print("=" * 70)
    print("Validating...")
    report = SoilValidator.validate(normalized)

    print("=" * 70)
    print("Generating Recommendations...")

    recommendations = RecommendationEngine.generate(
        report=report,
        crop=crop
    )

    print("\n")
    print("=" * 70)
    print(f"Crop : {crop}")
    print("=" * 70)

    for rec in recommendations:

        print(f"\nParameter     : {rec.parameter}")
        print(f"Value         : {rec.value}")
        print(f"Status        : {rec.status}")
        print(f"Fertilizer    : {rec.fertilizer}")
        print(f"Dose          : {rec.dose}")
        print(f"Purpose       : {rec.purpose}")
        print(f"Application   : {rec.application}")
        print(f"Precaution    : {rec.precaution}")
        print(f"Crop Note     : {rec.crop_note}")
        print("-" * 70)


if __name__ == "__main__":
    main()