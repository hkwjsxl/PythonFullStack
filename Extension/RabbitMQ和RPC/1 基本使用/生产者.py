import pika
from settings import *

# 有密码的连接
credentials = pika.PlainCredentials(RABBITMQ_SERVER_USER, RABBITMQ_SERVER_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_SERVER_HOST, credentials=credentials))
# 拿到channel对象
channel = connection.channel()
# 声明一个队列
channel.queue_declare(queue=QUEUE_NAME)  # 指定队列名字
# 生产者向队列中放一条消息
channel.basic_publish(exchange='',
                      routing_key=QUEUE_NAME,  # 必须和消费者中的队列名字一样
                      body='this is body/content')
print("sent success")
# 关闭连接
connection.close()
