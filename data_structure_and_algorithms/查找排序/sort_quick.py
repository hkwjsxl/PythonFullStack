"""快速排序"""
import random


# 方式一
# def quick_sort(arr, left=None, right=None):
#     left = 0 if not isinstance(left, (int, float)) else left
#     right = len(arr) - 1 if not isinstance(right, (int, float)) else right
#     if left < right:
#         partitionIndex = partition(arr, left, right)
#         quick_sort(arr, left, partitionIndex - 1)
#         quick_sort(arr, partitionIndex + 1, right)
#     return arr
#
#
# def partition(arr, left, right):
#     pivot = left
#     index = pivot + 1
#     i = index
#     while i <= right:
#         if arr[i] < arr[pivot]:
#             swap(arr, i, index)
#             index += 1
#         i += 1
#     swap(arr, pivot, index - 1)
#     return index - 1
#
#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]

# 方式二
def quick_sort(lst):
    # 让外界之传入一个参数即可
    _quick_sort(lst, 0, len(lst) - 1)


def _quick_sort(lst, left, right):
    if left < right:
        mid = partition(lst, left, right)
        _quick_sort(lst, left, mid - 1)
        _quick_sort(lst, mid + 1, right)


def partition(lst, left, right):
    current = lst[left]  # 选取第一个值为分割点
    while left < right:  # left和right相等时结束
        while current <= lst[right] and left < right:
            right -= 1
        lst[left] = lst[right]
        while current >= lst[left] and left < right:
            left += 1
        lst[right] = lst[left]
    lst[left] = current  # 最后把选取的值放到左边的空位中
    return left  # 最后left和right是相等的，返回哪个都一样


lst = [random.randrange(10, 99) for i in range(10)]
print(lst)
quick_sort(lst)
print(lst)
