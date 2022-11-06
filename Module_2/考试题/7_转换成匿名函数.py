"""请把以下函数转化为python lambda匿名函数"""


def add(x, y):
    return x + y


def run():
    v1 = lambda x, y: x + y
    print(v1(1, 2))
    ...


if __name__ == '__main__':
    run()
