"""基于推导式一行代码生成1-100以内的偶数列表。"""


def run():
    lst = [i for i in range(1, 101) if i % 2 == 0]
    print(lst)
    ...


if __name__ == '__main__':
    run()
