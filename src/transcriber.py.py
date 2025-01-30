import mlx.core as mx
from mlx_whisper import load_model, transcribe
from .logger import logger
from .exceptions import TranscriptionError

class WhisperTranscriber:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        
    def load_model(self):
        try:
            config = settings.whisper_config
            self.model, self.tokenizer, _ = load_model(
                config["model"],
                quantize=config["quantized"]
            )
            mx.set_default_device(mx.gpu if config["device"] == "mps" else mx.cpu)
        except Exception as e:
            logger.error(f"Model loading failed: {str(e)}")
            raise TranscriptionError("Model initialization failed")

    def transcribe(self, audio_path: str) -> str:
        if not self.model:
            self.load_model()
            
        try:
            result = transcribe(
                self.model,
                self.tokenizer,
                audio_path,
                language="ru",
                temperature=0.0
            )
            return " ".join([s["text"] for s in result["segments"]])
        except Exception as e:
            logger.error(f"Transcription failed: {str(e)}")
            raise TranscriptionError("Audio processing error")