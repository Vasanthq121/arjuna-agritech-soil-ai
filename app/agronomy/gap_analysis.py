from dataclasses import dataclass

# Crop nutrient targets (kg/ha)
# These are starter values and can later be expanded
CROP_REQUIREMENTS = {
    "Groundnut": {
        "nitrogen": 25,
        "phosphorus": 50,
        "potassium": 50,
    },
    "Rice": {
        "nitrogen": 120,
        "phosphorus": 60,
        "potassium": 40,
    },
}


@dataclass
class NutrientGap:
    parameter: str
    soil_value: float
    target_value: float
    difference: float
    status: str


class GapAnalysis:

    @staticmethod
    def analyze(report):
        crop = report.crop

        targets = CROP_REQUIREMENTS.get(crop, {})

        gaps = []

        for item in report.parameters:

            if item.parameter not in targets:
                continue

            target = targets[item.parameter]
            difference = target - item.value

            if difference > 0:
                status = "Deficient"
            elif difference < 0:
                status = "Excess"
            else:
                status = "Adequate"

            gaps.append(
                NutrientGap(
                    parameter=item.parameter,
                    soil_value=item.value,
                    target_value=target,
                    difference=difference,
                    status=status,
                )
            )

        return gaps