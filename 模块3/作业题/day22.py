# 1.简述进程和线程的区别以及应用场景。
"""
进程的开销比线程要大，计算密集型用进程，IO密集型用线程
进程：大量的数据计算
线程：网络传输，爬虫，文件读写
"""

# 2.什么是GIL锁
"""
全局解释器锁，CPython独有的，在单个进程中同一时刻只能有一个线程可以被CPU调用
"""

# 3.手写单例模式
"""
from threading import Thread, RLock

class Singleton:
    instance = None
    rlock = RLock()
    
    def __init__(self, name):
        self.name = name
    
    def __new__(cls, *args, **kwargs):
        with cls.rlock:
            if cls.instance:
                return cls.instance
        
            cls.instance = object.__new__(cls)
        return cls.instance

def func(name):
    t = Singleton(name)
    print(t)

for i in range(10):
    t = Thread(target=func, args=(i, ))
    t.start()

"""

# 9.data.txt 文件中共有 10000 条数据，请为每 100行 数据创建一个线程，并在线程中把当前100条数据的num列相加并打印。
from threading import Thread


def task(data_list):
    num_list = [int(i.split(',')[-1]) for i in data_list]
    print(sum(num_list))


def run():
    with open('data.txt', 'r', encoding='utf-8') as f:
        f.readline()
        data_list = []
        for line in f:
            data_list.append(line.strip())
            if len(data_list) == 2:
                t = Thread(target=task, args=(data_list,))
                t.start()
                data_list = []
        if data_list:
            t = Thread(target=task, args=(data_list,))
            t.start()


if __name__ == '__main__':
    run()
