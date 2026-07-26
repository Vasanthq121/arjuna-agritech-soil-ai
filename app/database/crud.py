from app.database.models import SoilParameter
from app.database.models import SoilReport


def save_report(db, data):

    report = SoilReport(
        farmer_name=data["farmer_name"],
        sample_id=data["sample_id"],
        crop=data["crop"],
        location=data["location"],
        sample_date=data["sample_date"],
        report_date=data["report_date"],
    )

    db.add(report)
    db.flush()

    for item in data["parameters"]:

        db.add(
            SoilParameter(
                report_id=report.id,
                parameter=item["parameter"],
                value=item["value"],
                unit=item["unit"],
                rating=item["rating"],
                remark=item["remark"],
            )
        )

    db.commit()

    db.refresh(report)

    return report