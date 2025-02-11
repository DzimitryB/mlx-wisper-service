import pika
from config.settings import settings

# Устанавливаем параметры соединения
connection_params = pika.ConnectionParameters(
                settings.rabbitmq_url,
                heartbeat=600,
                blocked_connection_timeout=600
            )

# Создаём соединение
connection = pika.BlockingConnection(connection_params)

# Выводим значение blocked_connection_timeout
print("🔍 blocked_connection_timeout =", connection_params.blocked_connection_timeout)

# Закрываем соединение
connection.close()