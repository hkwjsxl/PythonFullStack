"""单例模式"""


class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "%s" % self.value


if __name__ == '__main__':
    s1 = Singleton(10)
    s2 = Singleton(20)
    print(s1)
    print(s2)
