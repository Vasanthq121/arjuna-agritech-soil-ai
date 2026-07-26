from dataclasses import dataclass

from app.recommendation.crop_db import CROP_DB
from app.recommendation.fertilizer_db import FERTILIZER_DB


@dataclass
class Recommendation:
    parameter: str
    value: float
    status: str
    fertilizer: str
    dose: str
    purpose: str
    application: str
    precaution: str
    crop_note: str


class RecommendationEngine:

    # Default threshold values
    # These can later be moved to a database or configuration file.
    LIMITS = {
        "ph": (6.5, 7.5),
        "nitrogen": (280, 560),
        "phosphorus": (22, 56),
        "potassium": (120, 280),
    }

    @classmethod
    def generate(cls, report, crop):

        recommendations = []

        crop_rules = CROP_DB.get(crop, {})

        for item in report.parameters:

            if item.parameter not in cls.LIMITS:
                continue

            value = item.value
            low, high = cls.LIMITS[item.parameter]

            # ------------------------
            # Determine status
            # ------------------------

            if value < low:
                status = "Low"

            elif value > high:
                status = "High"

            else:
                status = "Optimal"

            # ------------------------
            # Default values
            # ------------------------

            fertilizer = "-"
            dose = "-"
            purpose = "-"
            application = "-"
            precaution = "-"
            crop_note = "-"

            # ------------------------
            # Low nutrient
            # ------------------------

            if status == "Low":

                fert = FERTILIZER_DB.get(item.parameter)

                if fert:

                    fertilizer = fert["fertilizer"]
                    purpose = fert["purpose"]
                    application = fert["application"]
                    precaution = fert["precaution"]

                crop_data = crop_rules.get(item.parameter)

                if crop_data and "low" in crop_data:

                    dose = crop_data["low"]["dose"]
                    crop_note = crop_data["low"]["note"]

            # ------------------------
            # High nutrient
            # ------------------------

            elif status == "High":

                precaution = (
                    f"{item.parameter.capitalize()} is already high. "
                    "Avoid additional fertilizer application."
                )

            # ------------------------
            # Optimal nutrient
            # ------------------------

            else:

                purpose = "Current nutrient level is adequate."

            recommendations.append(

                Recommendation(

                    parameter=item.parameter,
                    value=value,
                    status=status,

                    fertilizer=fertilizer,
                    dose=dose,

                    purpose=purpose,
                    application=application,
                    precaution=precaution,

                    crop_note=crop_note

                )

            )

        return recommendations