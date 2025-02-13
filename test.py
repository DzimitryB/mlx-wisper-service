# test.py
# import redis
# import pika
from time import time
from datetime import datetime

# Подключение к Redis
# r = redis.Redis(host='localhost', port=6379, db=0)

# Создайте тестовую задачу
task_id = f"test_task_{datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')}"
# url = "https://youtu.be/PWgvGjAhvIw"  # пример видео
url = "https://www.youtube.com/watch?v=VE480xvyPxk&t=1s"

# Сохраните URL в Redis
# r.set(f"url:{task_id}", url)

# Отправьте задачу в очередь
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.basic_publish(
#     exchange='',
#     routing_key='transcription_tasks',
#     body=task_id
# )
# connection.close()

# Мониторинг статуса
status = "pending"  # Временное значение для статуса
while True:
    print(f"Status: {status}")
    if status == "completed":
        result = "Транскрибированный текст"  # Временное значение для результата
        print("Result:", result)  # первые 2000 символов
        break
    time.sleep(2)