"""希尔排序"""

import random


def insert_shell_gap(lst, gap):
    # 在直接插入排序的基础上将原来的1都改为gap
    for i in range(gap, len(lst)):
        tmp = lst[i]
        j = i - gap
        while j >= 0 and tmp < lst[j]:
            lst[j + gap] = lst[j]
            j -= gap
        lst[j + gap] = tmp


def shell_sort(lst):
    gap = len(lst) // 2
    while gap >= 1:
        insert_shell_gap(lst, gap)
        gap //= 2


lst = [random.randrange(10, 99) for i in range(10)]
print(lst)
shell_sort(lst)
print(lst)
