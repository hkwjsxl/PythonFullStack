from functools import wraps


def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('before')
        res = func(*args, **kwargs)
        print('after')
        return res

    return inner


@wrapper
def func(a1):
    return a1 + "傻叉"


@wrapper
def base(a1, a2):
    return a1 + a2 + '傻缺'


@wrapper
def foo(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4 + '傻蛋'


result = func('6')
print(result)
# base('6', '7')
# foo ('6', '7', '8', '9')
