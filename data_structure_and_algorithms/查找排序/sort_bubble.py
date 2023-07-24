"""冒泡排序"""

import random


# def bubble_sort(lst):
#     for i in range(len(lst) - 1):
#         for j in range(i + 1, len(lst)):
#             if lst[i] >= lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#         # print(lst)
#     return lst


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(lst)
    return lst


def bubble_sort_advanced(lst):
    # 冒泡排序优化
    for i in range(len(lst) - 1):
        flag = False
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                flag = True
        if not flag:
            break
        print(lst)
    return lst


lst = [random.randrange(10, 99) for i in range(10)]
print(lst)
ret = bubble_sort(lst)
# ret = bubble_sort_advanced(lst)
print(ret)
