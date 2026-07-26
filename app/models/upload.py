from pydantic import BaseModel


class UploadResponse(BaseModel):
    report_id: str
    filename: str
    file_type: str
    file_size: int
    status: str