from config.settings import settings
import mlx.core as mx
from mlx_whisper.load_models import load_model
from mlx_whisper.transcribe import transcribe
from .logger import logger
from .exceptions import TranscriptionError

class WhisperTranscriber:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        logger.info("WhisperTranscriber initialized")

    def load_model(self):
        try:
            logger.debug("Loading model configuration")
            config = settings.whisper_config
            logger.debug(f"Model configuration: {config}")
            
            self.model, self.tokenizer, _ = load_model(
                config["model"]
            )
            logger.info("Model and tokenizer loaded successfully")
            
        except Exception as e:
            logger.error(f"Model loading failed: {str(e)}")
            raise TranscriptionError("Model initialization failed")

    def transcribe(self, audio_path: str) -> str:
        if not self.model:
            logger.info("Model not loaded, calling load_model()")
            self.load_model()
            
        try:
            logger.info(f"Starting transcription for: {audio_path}")
            
            # Предположим, что функция transcribe принимает только один аргумент
            result = transcribe(audio_path)
            
            logger.info("Transcription completed successfully")
            return " ".join([s["text"] for s in result["segments"]])
        except Exception as e:
            logger.error(f"Transcription failed: {str(e)}")