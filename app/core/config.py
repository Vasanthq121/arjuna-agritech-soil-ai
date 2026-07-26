from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# Project Root
BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    # ===============================
    # Application
    # ===============================
    APP_NAME: str = "Soil AI Assistant"
    APP_VERSION: str = "1.0.0"

    # ===============================
    # Gemini
    # ===============================
    GEMINI_API_KEY: str

    # ===============================
    # PostgreSQL
    # ===============================
    DATABASE_URL: str

    # ===============================
    # ChromaDB
    # ===============================
    CHROMA_DB_PATH: str = str(BASE_DIR / "vector_store")

    # ===============================
    # Upload
    # ===============================
    UPLOAD_FOLDER: str = str(BASE_DIR / "uploads" / "original")

    MAX_UPLOAD_SIZE_MB: int = 20

    # ===============================
    # OCR
    # ===============================
    OCR_LANGUAGE: str = "en"

    # ===============================
    # Logging
    # ===============================
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore"
    )


settings = Settings()