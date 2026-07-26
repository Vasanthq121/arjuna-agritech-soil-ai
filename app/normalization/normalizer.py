from app.normalization.parameter_mapper import PARAMETER_MAP


class SoilNormalizer:

    @staticmethod
    def normalize(data: dict) -> dict:

        for item in data["parameters"]:

            name = item["parameter"].strip().lower()

            item["parameter"] = PARAMETER_MAP.get(
                name,
                name.replace(" ", "_")
            )

            try:
                item["value"] = float(item["value"])
            except Exception:
                item["value"] = None

        return data