# test.py
import redis
import pika

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Создайте тестовую задачу
task_id = "test_task_2"
# url = "https://youtu.be/PWgvGjAhvIw"  # пример видео
url = "https://www.youtube.com/watch?v=VE480xvyPxk&t=1s"

# Сохраните URL в Redis
r.set(f"url:{task_id}", url)

# Отправьте задачу в очередь
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.basic_publish(
    exchange='',
    routing_key='transcription_tasks',
    body=task_id
)
connection.close()

# Мониторинг статуса
import time
while True:
    status = r.get(task_id)
    print(f"Status: {status.decode() if status else 'pending'}")
    if status and b'completed' in status:
        result = r.get(f"result:{task_id}")
        print("Result:", result.decode()[:2000] + "...")  # первые 2000  символов
        break
    time.sleep(2)