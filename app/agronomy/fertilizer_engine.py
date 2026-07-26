from dataclasses import dataclass


@dataclass
class FertilizerRecommendation:
    nutrient: str
    fertilizer: str
    nutrient_required: float
    fertilizer_required: float
    unit: str = "kg/ha"


FERTILIZER_DATABASE = {
    "nitrogen": {
        "name": "Urea",
        "content": 0.46,
    },
    "phosphorus": {
        "name": "DAP",
        "content": 0.46,
    },
    "potassium": {
        "name": "MOP",
        "content": 0.60,
    },
}


class FertilizerEngine:

    @staticmethod
    def calculate(gaps):

        recommendations = []

        for gap in gaps:

            if gap.difference <= 0:
                continue

            fert = FERTILIZER_DATABASE[gap.parameter]

            fertilizer_amount = gap.difference / fert["content"]

            recommendations.append(
                FertilizerRecommendation(
                    nutrient=gap.parameter,
                    fertilizer=fert["name"],
                    nutrient_required=gap.difference,
                    fertilizer_required=round(fertilizer_amount, 2),
                )
            )

        return recommendations