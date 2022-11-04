# 写timer装饰器实现：计算fun函数执行时间，并将结果给 result，最终打印（不必使用datetime,使用time.time即可）。
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time() - start_time
        return end_time

    return inner


@timer
def func():
    time.sleep(1)
    pass


result = func()
print(result)
