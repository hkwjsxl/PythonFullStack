import pika
from settings import *

# 有密码的连接
credentials = pika.PlainCredentials(RABBITMQ_SERVER_USER, RABBITMQ_SERVER_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_SERVER_HOST, credentials=credentials))
# 拿到channel对象
channel = connection.channel()
# 声明一个队列
# durable=True开启持久化
channel.queue_declare(queue=QUEUE_NAME, durable=True)  # 指定队列名字
# 生产者向队列中放一条消息
channel.basic_publish(
    exchange='',
    routing_key=QUEUE_NAME,  # 必须和消费者中的队列名字一样
    body='this is body/content',
    properties=pika.BasicProperties(
        delivery_mode=2,
    )
)
print("sent success")
# 关闭连接
connection.close()
