import pika
from settings import *


def main():
    # 无密码的连接
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='101.133.225.166'))
    # 有密码的连接
    credentials = pika.PlainCredentials(RABBITMQ_SERVER_USER, RABBITMQ_SERVER_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_SERVER_HOST, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # on_message_callback回调函数，auto_ack自动确认
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    # 消费者会夯在这等待生产者生产东西
    main()
