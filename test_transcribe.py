from src.transcriber import WhisperTranscriber

audio_path = 'audio.mp3'
transcriber = WhisperTranscriber()

result = transcriber.transcribe(audio_path)
print(result)
