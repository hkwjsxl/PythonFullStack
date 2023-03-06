import pika
from settings import *


def main():
    credentials = pika.PlainCredentials(RABBITMQ_SERVER_USER, RABBITMQ_SERVER_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_SERVER_HOST, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    def callback(ch, method, properties, body):
        # 等待20秒，20秒内有其他的生产，会分配给另外的消费者
        import time
        time.sleep(20)
        print(" [x] Received %r" % body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # 配置一句话，谁闲置谁获取，没必要按照顺序一个一个来
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=False)

    channel.start_consuming()


if __name__ == '__main__':
    main()
