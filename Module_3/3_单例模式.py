import time
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
            time.sleep(0.1)
            cls.instance = object.__new__(cls)
        return cls.instance


def func(name):
    t = Singleton(name)
    print(t)


for i in range(10):
    t = Thread(target=func, args=(i,))
    t.start()
