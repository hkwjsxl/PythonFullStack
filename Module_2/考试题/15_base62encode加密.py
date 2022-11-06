"""编写函数，实现base62encode加密（62进制），例如："""
"""
内部维护的数据有：0123456789AB..Zab..z(10个数字+26个大写字母+26个小写字母)。
当执行函数：
	base62encode(1)，获取的返回值为1
	base62encode(61)，获取的返回值为z
	base62encode(62)，获取的返回值为10
"""
import string
import itertools


# def base62encode(num):
#     # datas = string.digits + string.ascii_uppercase + string.ascii_lowercase
#     data_list = list(itertools.chain(string.digits, string.ascii_uppercase, string.ascii_lowercase))
#     list_len = len(data_list)
#     v = ''
#     while num >= list_len:
#         v1, num = divmod(num, list_len)
#         v += data_list[v1]
#         if v1 < list_len:
#             return v + data_list[num]
#     return data_list[num]


def base62encode(num):
    MAP = list(itertools.chain(string.digits, string.ascii_uppercase, string.ascii_lowercase))
    total_count = len(MAP)
    position_value = []
    while num >= total_count:
        num, remain = divmod(num, total_count)
        position_value.insert(0, MAP[remain])
    position_value.insert(0, MAP[num])

    result = "".join(position_value)
    return result


def run():
    result = base62encode(61)
    print(result)
    result = base62encode(108)
    print(result)
    result = base62encode(1024)
    print(result)


if __name__ == '__main__':
    run()
