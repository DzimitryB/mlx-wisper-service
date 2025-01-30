import pika
from loguru import logger
from .exceptions import QueueConnectionError
from config.settings import settings

class QueueClient:
    def __init__(self):
        self.connection = None
        self.channel = None

    def connect(self):
        try:
            self.connection = pika.BlockingConnection(
                pika.URLParameters(settings.rabbitmq_url)
            )
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='transcription_tasks', durable=True)
            logger.success("Connected to RabbitMQ")
        except Exception as e:
            logger.error(f"Queue connection failed: {str(e)}")
            raise QueueConnectionError("Can't connect to message queue")

    def close(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
            logger.info("Queue connection closed")