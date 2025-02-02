from config.settings import settings
from yt_dlp import YoutubeDL
from loguru import logger
from pathlib import Path
from .exceptions import DownloadError  # Убедитесь, что exceptions.py существует

def download_audio(url: str) -> str:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': settings.audio_settings['format'],
            'preferredquality': settings.audio_settings['bitrate'],
        }],         
        'verbose': False,
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        },
        'ffmpeg_location': settings.ffmpeg_location
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            original_path = ydl.prepare_filename(info)
            return str(Path(original_path).with_suffix('.mp3'))
            
    except Exception as e:
        logger.error(f"Download failed: {str(e)}")
        raise DownloadError("Video download error") from e