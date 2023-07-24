"""归并排序"""

import random


def merge(lst, low, mid, high):
    """
    完成一次归并
    :param lst: 列表
    :param low: 左端的起点
    :param mid: 左端的终点
    :param high: 右端(整体)的终点
    :return:
    """
    i = low  # 列表左端开头
    j = mid + 1  # 列表右端开头
    tmp_list = []
    while i <= mid and j <= high:
        if lst[i] < lst[j]:
            tmp_list.append(lst[i])
            i += 1
        else:
            tmp_list.append(lst[j])
            j += 1
    # 跳出循环说明 左端或右端的列表循环完了
    while i <= mid:  # 如果是左边没有循环完
        tmp_list.append(lst[i])
        i += 1
    while j <= high:  # 如果是右边没有循环完
        tmp_list.append(lst[j])
        j += 1
    # 赋值给原来的列表
    lst[low:high + 1] = tmp_list


def _merge_sort(lst, low, high):
    if low < high:  # low等于high说明列表只有一个元素
        mid = (low + high) // 2
        _merge_sort(lst, low, mid)  # 左边排序
        _merge_sort(lst, mid + 1, high)  # 右边排序
        merge(lst, low, mid, high)  # 归并一次


def merge_sort(lst):
    # 让外界只传入一个列表即可
    _merge_sort(lst, 0, len(lst) - 1)


lst = [random.randrange(10, 99) for i in range(10)]
print(lst)
merge_sort(lst)
print(lst)
