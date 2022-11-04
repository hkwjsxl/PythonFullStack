"""列表推导式和生成器表达式 [i % 2 for i in range(10)] 和 (i % 2 for i in range(10)) 输出结果分别是什么？"""


def run():
    lst = [i % 2 for i in range(10)]
    tup = (i % 2 for i in range(10))
    print(lst)
    print(tup)
    ...


if __name__ == '__main__':
    run()
