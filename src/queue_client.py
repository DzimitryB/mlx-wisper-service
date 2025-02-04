import pika
from loguru import logger
from .exceptions import QueueConnectionError
from config.settings import settings


class QueueClient:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.blocked_connection_timeout = 600
        self.heartbeat = 600

    def connect(self):
        try:
            # Создаем параметры соединения
            connection_params = pika.ConnectionParameters(
                settings.rabbitmq_url,
                heartbeat=self.heartbeat,
                blocked_connection_timeout=self.blocked_connection_timeout
            )

            
            # Устанавливаем соединение с использованием параметров
            self.connection = pika.BlockingConnection(connection_params)
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='transcription_tasks', durable=True)
            logger.success("Connected to RabbitMQ")
        except Exception as e:
            logger.error(f"Queue connection failed: {str(e)}")
            raise QueueConnectionError("Can't connect to message queue")

    def close(self):
        if self.connection and self.connection.is_open:
            self.connection.close()