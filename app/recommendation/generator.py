import json

import google.generativeai as genai

from app.core.config import settings


genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")


class RecommendationGenerator:

    @staticmethod
    def generate(prompt):

        response = model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)