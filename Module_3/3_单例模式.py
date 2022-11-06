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

"""
class Singleton(object):

    def __init__(self):
        print("__init__")

    def __new__(cls, *args, **kwargs):
        print("__new__")
        if not hasattr(Singleton, "_instance"):
            print(" 创建新实例 ")
            Singleton._instance = object.__new__(cls)
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)


"""

"""
# 改进：让__init__方法仅执行一次


class Singleton(object):

    def __init__(self):
        if not hasattr(Singleton, "_first_init"):
            print("__init__")
            Singleton._first_init = True

    def __new__(cls, *args, **kwargs):
        print("__new__")
        if not hasattr(Singleton, "_instance"):
            print("创建新实例")
            Singleton._instance = object.__new__(cls)
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)
"""