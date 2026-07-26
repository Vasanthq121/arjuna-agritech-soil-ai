from typing import List

from pydantic import BaseModel


class SoilParameter(BaseModel):
    parameter: str
    value: float
    unit: str
    rating: str
    remark: str


class SoilReport(BaseModel):
    farmer_name: str
    sample_id: str
    crop: str
    location: str
    sample_date: str
    report_date: str
    parameters: List[SoilParameter]