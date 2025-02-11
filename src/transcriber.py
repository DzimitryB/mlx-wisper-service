from config.settings import settings
import mlx.core as mx
from mlx_whisper.load_models import load_model
from mlx_whisper.transcribe import transcribe
from .exceptions import TranscriptionError

class WhisperTranscriber:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        config = settings.whisper_config
        self.model, self.tokenizer, _ = load_model(config["model"])

    def transcribe(self, audio_path: str) -> str:
        result = transcribe(audio_path)
        return " ".join([s["text"] for s in result["segments"]])