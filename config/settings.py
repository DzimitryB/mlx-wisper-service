import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    @property
    def whisper_config(self):
        return {
            "model": os.getenv("WHISPER_MODEL", "base"),
            "quantized": os.getenv("WHISPER_QUANTIZED", "True") == "True",
            "device": os.getenv("WHISPER_DEVICE", "mps")
        }
    
    @property
    def redis_url(self):
        return os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    @property
    def rabbitmq_url(self):
        return os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")

settings = Settings()