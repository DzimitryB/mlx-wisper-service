# Transcription Service (MLX-Whisper)

Микросервис для транскрипции видео/аудио с использованием MLX.

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
└── main.py