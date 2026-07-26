from pathlib import Path

from fastapi import HTTPException, UploadFile

from app.core.config import settings
from app.core.logger import logger
from app.models.upload import UploadResponse
from app.utils.file_utils import (
    generate_report_id,
    get_extension,
    is_allowed,
)


class UploadService:

    @staticmethod
    async def save(file: UploadFile) -> UploadResponse:

        if not file.filename:
            raise HTTPException(status_code=400, detail="Filename missing")

        if not is_allowed(file.filename):
            raise HTTPException(
                status_code=400,
                detail="Only PDF, PNG, JPG and JPEG files are supported."
            )

        report_id = generate_report_id()
        extension = get_extension(file.filename)

        upload_dir = Path(settings.UPLOAD_FOLDER)
        upload_dir.mkdir(parents=True, exist_ok=True)

        destination = upload_dir / f"{report_id}{extension}"

        contents = await file.read()

        max_size = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024

        if len(contents) > max_size:
            raise HTTPException(
                status_code=413,
                detail=f"Maximum upload size is {settings.MAX_UPLOAD_SIZE_MB} MB."
            )

        with open(destination, "wb") as f:
            f.write(contents)

        logger.info("Saved report %s", report_id)

        return UploadResponse(
            report_id=report_id,
            filename=destination.name,
            file_type=extension.replace(".", "").upper(),
            file_size=len(contents),
            status="uploaded",
        )