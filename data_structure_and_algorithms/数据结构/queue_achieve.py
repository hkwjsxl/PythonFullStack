"""
环形队列：当队尾指针front == Maxsize + 1时，再前进一个位置就自动到0.
队首指针前进1：front = (front + 1) % MaxSize
队尾指针前进1：rear = (rear + 1) % MaxSize
队空条件：rear == front
队满条件：(rear + 1) % MaxSize == front
"""


class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.rear = 0
        self.front = 0
        self.size = size

    def push(self, value):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
        else:
            # 一、队列满就顶掉最前面的一个元素
            self.front = (self.front + 1) % self.size
            self.rear = (self.rear + 1) % self.size
            self.queue[self.front] = value
            # 二、队列满报错
            # raise IndexError("queue is filled.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        raise IndexError("queue is empty.")

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)
print(q.is_empty())
for i in range(4):
    q.push(i)
print(q.is_filled())
print(q.pop())
