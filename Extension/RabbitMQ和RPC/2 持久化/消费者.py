import pika
from settings import *


def main():
    # 有密码的连接
    credentials = pika.PlainCredentials(RABBITMQ_SERVER_USER, RABBITMQ_SERVER_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_SERVER_HOST, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        # 真正的消息处理完了，再发确认
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=False)

    channel.start_consuming()


if __name__ == '__main__':
    # 消费者会夯在这等待生产者生产东西
    main()
