from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os

from app.services.soil_analysis_service import SoilAnalysisService

router = APIRouter()


@router.post("/analyze")
async def analyze(
    crop: str = Form(...),
    file: UploadFile = File(...)
):

    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    pdf_path = os.path.join(upload_dir, file.filename)

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = SoilAnalysisService.analyze(
        pdf_path=pdf_path,
        crop=crop
    )

    return result