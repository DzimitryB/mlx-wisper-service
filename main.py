from src import (
    WhisperTranscriber,
    download_audio,
    QueueClient,
    logger
)
from src.exceptions import DownloadError, TranscriptionError
import redis
from config.settings import settings

def main():
    # Инициализация компонентов
    transcriber = WhisperTranscriber()
    queue_client = QueueClient()
    
    try:
        # Подключение к Redis
        redis_conn = redis.Redis.from_url(settings.redis_url)
        logger.info("Connected to Redis")

        # Подключение к очереди
        queue_client.connect()

        def callback(ch, method, properties, body):
            task_id = body.decode()
            try:
                redis_conn.set(task_id, "processing")
                url = redis_conn.get(f"url:{task_id}").decode()
                
                logger.info(f"Processing task {task_id}: {url}")
                
                # Скачивание аудио
                audio_path = download_audio(url)
                
                # Транскрипция
                text = transcriber.transcribe(audio_path)
                
                # Сохранение результата
                redis_conn.set(task_id, "completed")
                redis_conn.set(f"result:{task_id}", text)
                logger.success(f"Task {task_id} completed")

            except DownloadError as e:
                error_msg = f"Download error: {str(e)}"
                redis_conn.set(task_id, error_msg)
                logger.error(error_msg)
            except TranscriptionError as e:
                error_msg = f"Transcription error: {str(e)}"
                redis_conn.set(task_id, error_msg)
                logger.error(error_msg)
            except Exception as e:
                error_msg = f"Unexpected error: {str(e)}"
                redis_conn.set(task_id, error_msg)
                logger.critical(error_msg)

        # Настройка потребителя очереди
        queue_client.channel.basic_consume(
            queue='transcription_tasks',
            on_message_callback=callback,
            auto_ack=True
        )

        logger.info("Service started. Waiting for tasks...")
        queue_client.channel.start_consuming()

    except KeyboardInterrupt:
        logger.info("Shutting down service...")
        queue_client.close()
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}")
        raise

if __name__ == "__main__":
    main()