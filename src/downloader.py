from pytube import YouTube
from loguru import logger
from .exceptions import DownloadError

def download_audio(url: str) -> str:
    try:
        if "youtube.com" in url or "youtu.be" in url:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            return stream.download(filename="audio.mp4")
        else:
            raise DownloadError("Unsupported video platform")
    except Exception as e:
        logger.error(f"Download failed: {str(e)}")
        raise DownloadError("Video download error")