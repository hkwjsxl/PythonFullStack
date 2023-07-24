"""选择排序"""

import random


def select_sort_simple(lst):
    # 简单版
    # 每一趟找出最小的数，放到列表中
    ret_list = []
    for i in range(len(lst)):
        min_num = min(lst)
        ret_list.append(min_num)
        lst.remove(min_num)
    return ret_list


def select_sort(lst):
    for i in range(len(lst) - 1):
        mix_loc = i  # 记录最小的坐标
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[mix_loc]:
                mix_loc = j
        lst[i], lst[mix_loc] = lst[mix_loc], lst[i]
    return lst


lst = [random.randrange(10, 99) for i in range(10)]
print(lst)
# ret = select_sort_simple(lst)
ret = select_sort(lst)
print(ret)
