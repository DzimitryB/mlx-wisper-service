import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    @property
    def whisper_config(self):
        return {
            "model": os.getenv("WHISPER_MODEL", "mlx_models/tiny")
        }
    
    @property
    def redis_url(self):
        return os.getenv("REDIS_URL", "redis://localhost:6379/0")
    

    @property
    def rabbitmq_config(self):
        return {
            'host':os.getenv('RABBITMQ_HOST', 'localhost'),
            'port':int(os.getenv('RABBITMQ_PORT', 5672)),
            'user':os.getenv('RABBITMQ_USER', 'guest'),
            'password':os.getenv('RABBITMQ_PASSWORD', 'guest'),
            'heartbeat':int(os.getenv('HEARTBEAT', 600)),
            'blocked_connection':int(os.getenv('BLOCKED_CONNECTION_TIMEOUT', 600))
        }
 
    
    @property
    def audio_settings(self):
        return {
            'bitrate': '128k',
            'format': 'mp3'
        }
    
    @property
    def ffmpeg_location(self):
        return '/opt/homebrew/bin/ffmpeg'
    
    @property
    def huggingface_api_key(self):
        return os.getenv("HUGGINGFACE_API_KEY", "hf_your_api_key")

settings = Settings()