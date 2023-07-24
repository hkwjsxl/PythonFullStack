"""
基数排序
两种方法的不同在于如何看待最大数的位数
"""

import random
import math


# 方法一
def radix_sort(lst, num=10):
    """
    :param lst: 列表
    :param num: 桶的数量
    :return:
    """
    max_value = max(lst)  # 拿到最大的数
    length = int(math.log(max_value, 10)) + 1  # 直接获取最大数的位数，log的第二个参数表示以什么为底
    i = 0
    while length > 0:
        bucket_list = [[] for _ in range(num)]  # 创建桶
        for value in lst:
            # ps: 987 i=0:987%10-->7 i=1:987//10%10-->8 i=2:987//100%10-->9
            digit = value // 10 ** i % 10  # 求出当前数的个位、百位、千位...
            bucket_list[digit].append(value)
        lst.clear()
        for li in bucket_list:
            lst.extend(li)
        length -= 1
        i += 1


# 方法二
def radix_sort(lst, num=10):
    """
    :param lst: 列表
    :param num: 桶的数量
    :return:
    """
    max_value = max(lst)  # 拿到最大的数
    i = 0  # 不直接获取最大数的位数
    while 10 ** i <= max_value:
        bucket_list = [[] for _ in range(num)]  # 创建桶
        for value in lst:
            # ps: 987 i=0:987%10-->7 i=1:987//10%10-->8 i=2:987//100%10-->9
            digit = value // 10 ** i % 10  # 求出当前数的个位、百位、千位...
            bucket_list[digit].append(value)
        lst.clear()
        for li in bucket_list:
            lst.extend(li)
        i += 1


lst = [random.randrange(1, 999) for i in range(10)]
print(lst)
radix_sort(lst)
print(lst)
