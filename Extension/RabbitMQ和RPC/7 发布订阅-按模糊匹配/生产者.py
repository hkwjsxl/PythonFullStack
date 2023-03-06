import pika
from settings import *

credentials = pika.PlainCredentials(RABBITMQ_SERVER_USER, RABBITMQ_SERVER_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_SERVER_HOST, credentials=credentials))
channel = connection.channel()

# 声明队列没有指定名字，指定了exchange
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic')
message = "info: publish"
channel.basic_publish(
    exchange=EXCHANGE_NAME,
    routing_key=ROUTING_KEY,
    body=message,
)
print("sent success")
connection.close()
