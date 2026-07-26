from dataclasses import dataclass


@dataclass
class NutrientInteraction:
    source: str
    affected: str
    effect: str


MULDER_RULES = {
    "phosphorus": [
        NutrientInteraction(
            source="phosphorus",
            affected="zinc",
            effect="High phosphorus may reduce zinc availability.",
        )
    ],
    "potassium": [
        NutrientInteraction(
            source="potassium",
            affected="magnesium",
            effect="Excess potassium may reduce magnesium uptake.",
        )
    ],
    "nitrogen": [
        NutrientInteraction(
            source="nitrogen",
            affected="potassium",
            effect="High nitrogen may increase potassium requirement.",
        )
    ],
}


class MulderEngine:

    @staticmethod
    def analyze(gaps):

        warnings = []

        for gap in gaps:

            if gap.status != "Excess":
                continue

            warnings.extend(
                MULDER_RULES.get(gap.parameter, [])
            )

        return warnings