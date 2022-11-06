from functools import wraps
import os


def wrapper(func):
    @wraps(func)
    def inner(path, *args, **kwargs):
        dir_path, file_path = os.path.split(path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        res = func(path, *args, **kwargs)
        return res

    return inner


@wrapper
def write_user_info(path):
    file_obj = open(path, mode='w', encoding='utf-8')
    file_obj.write("武沛齐")
    file_obj.close()


write_user_info(r'files/bin/xxx/xxx.png')
