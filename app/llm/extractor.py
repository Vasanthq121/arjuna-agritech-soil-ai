import json

from app.llm.gemini_client import generate
from app.llm.prompts import SOIL_EXTRACTION_PROMPT


class SoilExtractor:

    @staticmethod
    def extract(report: str):

        prompt = SOIL_EXTRACTION_PROMPT.replace(
            "{report}",
            report
        )

        response = generate(prompt)

        cleaned = response.strip()

        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]

        elif cleaned.startswith("```"):
            cleaned = cleaned[3:]

        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]

        cleaned = cleaned.strip()

        return json.loads(cleaned)