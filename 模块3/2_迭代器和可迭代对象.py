from collections.abc import Iterator, Iterable


def run():
    v1 = [1,2,3]
    v2 = v1.__iter__()
    print(isinstance(v2, Iterator))
    if isinstance(v1, Iterable) and not isinstance(v1, Iterator):
        print(f'{v1}是可迭代对象')


if __name__ == '__main__':
    run()
