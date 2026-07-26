from fastapi import APIRouter, File, UploadFile

from app.models.upload import UploadResponse
from app.services.upload_service import UploadService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/", response_model=UploadResponse)
async def upload_report(
    file: UploadFile = File(...)
):
    return await UploadService.save(file)