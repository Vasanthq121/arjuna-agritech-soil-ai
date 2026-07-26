from app.core.config import settings
from app.core.logger import logger

logger.info("Configuration Loaded Successfully")

print(settings.APP_NAME)
print(settings.DATABASE_URL)
print(settings.UPLOAD_FOLDER)