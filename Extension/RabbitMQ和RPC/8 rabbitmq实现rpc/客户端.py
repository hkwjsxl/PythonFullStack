import pika
import uuid
from settings import *


class FibonacciRpcClient(object):

    def __init__(self):

        self.credentials = pika.PlainCredentials(RABBITMQ_SERVER_USER, RABBITMQ_SERVER_PASSWORD)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(RABBITMQ_SERVER_HOST, credentials=self.credentials)
        )
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue=QUEUE_NAME_CLIENT, exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=EXCHANGE_NAME_CLIENT,
            routing_key=ROUTING_KEY,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(5)")
response = fibonacci_rpc.call(10)  # 外界看上去，就像调用本地的call()函数一样
print(" [.] Got %r" % response)
