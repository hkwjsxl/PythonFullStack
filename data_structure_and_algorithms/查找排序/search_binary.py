"""二分查找(必须是排好序的内容)"""


def binary_search(lst, val):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if val > lst[mid]:
            low = mid + 1
        elif val < lst[mid]:
            high = mid - 1
        else:
            return mid
    return


ret = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print(ret)
