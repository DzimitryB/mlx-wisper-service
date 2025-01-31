# Transcription Service (MLX-Whisper)

Микросервис для транскрипции видео/аудио с использованием MLX.


## Environment Variables

| Переменная | Описание |
|------------|----------|
| RABBITMQ_URL | URL RabbitMQ |
| REDIS_URL | URL Redis |
| WHISPER_MODEL | Модель (tiny, base, etc) |
| WHISPER_QUANTIZED | Использовать квантование |
| WHISPER_DEVICE | mps/cpu |

## API Endpoints

POST /transcribe - Запуск транскрипции

## Features
- Поддержка YouTube и прямых ссылок на видео
- Транскрипция через MLX-Whisper (оптимизировано для Apple Silicon)
- Интеграция с RabbitMQ и Redis
- Конфигурация через переменные окружения

## Quick Start
```bash
git clone https://github.com/your-repo/transcription-service
cd transcription-service

# Заполните .env
cp .env.example .env

# Запуск с Docker
docker-compose up --build

# Локальный запуск
pip install -r requirements.txt
python main.py
```

## Структура проекта

```
transcription-service/
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
├── requirements.txt
├── config/
│   └── settings.py
├── src/
│   ├── __init__.py
│   ├── downloader.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── queue_client.py
│   └── transcriber.py
├── main.py
├── test.py

## Quick test run
```bash

# ForMacOS
# Install libraries
brew install ffmpeg redis rabbitmq

# Run services
brew services start rabbitmq
brew services start redis

# apply virtual environment
cd transcription-service
python -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# copy and configure .env
cp .env.example .env
nano .env  # fill in BOT_TOKEN and other variables if needed

# run service
python main.py

# run test
python test.py
```
