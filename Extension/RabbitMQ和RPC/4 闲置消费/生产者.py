import pika
from settings import *

credentials = pika.PlainCredentials(RABBITMQ_SERVER_USER, RABBITMQ_SERVER_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_SERVER_HOST, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME, durable=True)
channel.basic_publish(
    exchange='',
    routing_key=QUEUE_NAME,
    body='this is body/content',
    properties=pika.BasicProperties(
        delivery_mode=2,
    )
)
print("sent success")
connection.close()
