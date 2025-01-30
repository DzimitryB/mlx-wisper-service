import pika
import redis
from loguru import logger
from src import WhisperTranscriber, download_audio
from config.settings import settings

def main():
    # Инициализация компонентов
    transcriber = WhisperTranscriber()
    r = redis.Redis.from_url(settings.redis_url)
    
    # Подключение к RabbitMQ
    connection = pika.BlockingConnection(pika.URLParameters(settings.rabbitmq_url))
    channel = connection.channel()
    channel.queue_declare(queue='transcription_tasks')

    def callback(ch, method, properties, body):
        task_id = body.decode()
        try:
            r.set(task_id, "processing")
            url = r.get(f"url:{task_id}").decode()
            
            # Скачивание и транскрипция
            audio_path = download_audio(url)
            text = transcriber.transcribe(audio_path)
            
            r.set(task_id, "completed")
            r.set(f"result:{task_id}", text)
            
        except Exception as e:
            r.set(task_id, f"error: {str(e)}")
            logger.error(f"Task failed: {task_id}")

    channel.basic_consume(
        queue='transcription_tasks',
        on_message_callback=callback,
        auto_ack=True
    )

    logger.info("Service started. Waiting for tasks...")
    channel.start_consuming()

if __name__ == "__main__":
    main()