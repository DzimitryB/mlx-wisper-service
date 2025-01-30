from loguru import logger
import sys

def configure_logger():
    logger.remove()
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{module}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        level="INFO"
    )
    logger.add(
        "logs/transcription.log",
        rotation="10 MB",
        retention="7 days",
        level="DEBUG"
    )
    return logger

logger = configure_logger()