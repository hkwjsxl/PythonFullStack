"""计数排序"""

import random


def count_sort(lst, max_count=100):
    """
    :param lst: 列表
    :param max_count: 列表中最大的数值
    :return:
    """
    tmp_list = [0 for i in range(max_count + 1)]  # 长度为max_count的全为0的数组
    for val in lst:
        tmp_list[val] += 1
    i = 0
    for index, value in enumerate(tmp_list):
        for v in range(value):
            lst[i] = index
            i += 1


lst = [random.randrange(1, 99) for i in range(100)]
print(lst)
count_sort(lst)
print(lst)
