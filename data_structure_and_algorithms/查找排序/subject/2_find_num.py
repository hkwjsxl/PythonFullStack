"""
给定⼀个m*n的⼆维列表，查找⼀个数是否存在。列表有下列特性：
每⼀⾏的列表从左到右已经排序好。
每⼀⾏第⼀个数⽐上⼀⾏最后⼀个数⼤。
"""


# 方法一
def find_num(nums, target):
    """
    :param nums: 二维列表
    :param target: 目标数字
    :return: 存在返回True，反之返回False
    """
    tmp_list = []
    for li in nums:
        tmp_list.extend(li)
    # print(tmp_list)  # [2, 9, 11, 13, 15, 27, 56, 78, 97, 100, 112, 130]
    low = 0
    high = len(tmp_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if target < tmp_list[mid]:
            high = mid - 1
        elif target > tmp_list[mid]:
            low = mid + 1
        else:
            return True
    return False


# 方法二
def find_num(nums, target):
    """
    :param nums: 二维列表
    :param target: 目标数字
    :return: 存在返回True，反之返回False
    """
    h = len(nums)  # 行数
    if h == 0:
        return False
    w = len(nums[0])  # 列数
    if w == 0:
        return False
    left = 0
    right = h * w - 1
    while left <= right:
        mid = (left + right) // 2
        # 确定当前数的位置
        i = mid // w  # 行
        j = mid % w  # 列
        if target < nums[i][j]:
            right = mid - 1
        elif target > nums[i][j]:
            left = mid + 1
        else:
            return True
    return False


result = find_num(
    [
        [2, 9, 11],
        [13, 15, 27],
        [56, 78, 97],
        [100, 112, 130],
    ],
    78
)
print(result)
result = find_num([], 78)
print(result)
