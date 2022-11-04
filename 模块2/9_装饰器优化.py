from functools import wraps


def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return inner


@wrapper  # main = warpper(main)
def main():
    """
    main-注释
    :return:
    """
    print('main函数执行')
    print(main.__name__)  # 获取函数名
    print(main.__doc__)  # 获取函数的注释


if __name__ == '__main__':
    main()
