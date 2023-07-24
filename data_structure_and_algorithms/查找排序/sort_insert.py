"""插入排序"""

import random


def insert_sort(lst):
    for i in range(1, len(lst)):  # 第一个是有序区
        current_val = lst[i]
        j = i - 1  # 前面排好序的最大索引
        while current_val < lst[j] and j >= 0:  # 前面有序的值比摸到的大，就换位置，并且j=-1的时候表示前面已经遍历完了
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current_val
    return lst


lst = [random.randrange(10, 99) for i in range(10)]
print(lst)
ret = insert_sort(lst)
print(ret)
