from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database.database import Base


class SoilReport(Base):

    __tablename__ = "soil_reports"

    id = Column(Integer, primary_key=True, index=True)

    farmer_name = Column(String)
    sample_id = Column(String, unique=True)
    crop = Column(String)
    location = Column(String)
    sample_date = Column(String)
    report_date = Column(String)

    parameters = relationship(
        "SoilParameter",
        back_populates="report",
        cascade="all, delete-orphan"
    )


class SoilParameter(Base):

    __tablename__ = "soil_parameters"

    id = Column(Integer, primary_key=True)

    report_id = Column(
        Integer,
        ForeignKey("soil_reports.id")
    )

    parameter = Column(String)
    value = Column(Float)
    unit = Column(String)
    rating = Column(String)
    remark = Column(String)

    report = relationship(
        "SoilReport",
        back_populates="parameters"
    )