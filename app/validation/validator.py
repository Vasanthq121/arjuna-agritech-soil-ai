from pydantic import ValidationError

from app.validation.rules import SOIL_LIMITS
from app.validation.schema import SoilReport


class SoilValidator:

    @staticmethod
    def validate(data: dict) -> SoilReport:

        report = SoilReport.model_validate(data)

        for item in report.parameters:

            if item.parameter in SOIL_LIMITS:

                low, high = SOIL_LIMITS[item.parameter]

                if not (low <= item.value <= high):
                    raise ValueError(
                        f"{item.parameter} value {item.value} is outside "
                        f"the allowed range ({low} - {high})"
                    )

        return report