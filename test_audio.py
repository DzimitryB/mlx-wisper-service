from src import download_audio, DownloadError

try:
    path = download_audio("https://youtu.be/dQw4w9WgXcQ")
    print(f"Audio saved to: {path}")
except DownloadError as e:
    print(f"Error: {str(e)}")