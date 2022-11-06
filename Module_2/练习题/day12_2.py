import random
from functools import wraps

"""将被装饰的函数执行5次，讲每次执行函数的结果按照顺序放到列表中，最终返回列表。"""


def wrapper(func):
    @wraps(func)
    def inner():
        lst = []
        for i in range(5):
            res = func()
            lst.append(res)
        return lst

    return inner


@wrapper
def func():
    return random.randint(1, 4)


result = func()  # 内部自动执行5次，并将每次执行的结果追加到列表最终返回给result
print(result)
