from dataclasses import dataclass


@dataclass
class CropRequirement:
    nitrogen: float
    phosphorus: float
    potassium: float


CROP_DATABASE = {
    "Rice": CropRequirement(
        nitrogen=120,
        phosphorus=60,
        potassium=40,
    ),
    "Groundnut": CropRequirement(
        nitrogen=25,
        phosphorus=50,
        potassium=50,
    ),
    "Maize": CropRequirement(
        nitrogen=150,
        phosphorus=75,
        potassium=50,
    ),
    "Cotton": CropRequirement(
        nitrogen=100,
        phosphorus=50,
        potassium=50,
    ),
}


class CropEngine:

    @staticmethod
    def get_requirement(crop_name: str) -> CropRequirement:
        crop = CROP_DATABASE.get(crop_name)

        if crop is None:
            raise ValueError(f"Crop '{crop_name}' is not supported.")

        return crop