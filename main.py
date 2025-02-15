from src import (
    WhisperTranscriber,
    download_audio,
    QueueClient,
    logger
)
from src.exceptions import QueueConnectionError
# import redis
# from config.settings import settings

def main():
    # Инициализация компонентов
    transcriber = WhisperTranscriber()
    queue_client = QueueClient()
    
    # Подключение к очереди
    try:
        queue_client.connect()  # Убедитесь, что соединение устанавливается
    except QueueConnectionError as e:
        logger.critical(f"Failed to connect to RabbitMQ: {str(e)}")
        return

    def callback(ch, method, properties, body):
        task_id = body.decode()
        # redis_conn.set(task_id, "processing")
        # url = # redis_conn.get(f"url:{task_id}").decode()
        url = "https://example.com/audio.mp3"  # Временное значение для тестирования
        
        audio_path = download_audio(url)
        text = transcriber.transcribe(audio_path)
        
        # redis_conn.set(task_id, "completed")
        # redis_conn.set(f"result:{task_id}", text)

    # Настройка потребителя очереди
    queue_client.channel.basic_consume(
        queue='transcription_tasks',
        on_message_callback=callback,
        auto_ack=True
    )

    queue_client.channel.start_consuming()

if __name__ == "__main__":
    main()