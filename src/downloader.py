from config.settings import settings
from yt_dlp import YoutubeDL
from pathlib import Path

def download_audio(url: str) -> str:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': settings.audio_settings['format'],
            'preferredquality': settings.audio_settings['bitrate'],
        }],
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'ffmpeg_location': settings.ffmpeg_location
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        original_path = ydl.prepare_filename(info)
        return str(Path(original_path).with_suffix('.mp3'))