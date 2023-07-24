"""桶排序"""

import random


def bucket_sort(lst, num=10, max_num=1000):
    """
    :param lst: 列表
    :param num: 桶的数量
    :param max_num: 最大数值
    :return:
    """
    tmp_list = [[] for _ in range(num)]  # 创建桶（二维数组）
    for value in lst:
        n = min(value // (max_num // num), num - 1)  # n表示将数值填入第几号桶（最大的数值要填入最后一个桶，所以要min一下）
        tmp_list[n].append(value)
        # 桶内排序
        for i in range(len(tmp_list[n]) - 1, -1, -1):
            if i - 1 >= 0 and tmp_list[n][i] < tmp_list[n][i - 1]:  # 如果前面的比后面的大，就换下位置
                tmp_list[n][i], tmp_list[n][i - 1] = tmp_list[n][i - 1], tmp_list[n][i]
            else:
                break
    # 将所有桶内元素放到新列表中
    sorted_list = []
    for li in tmp_list:
        sorted_list.extend(li)
    return sorted_list


lst = [random.randrange(1, 999) for i in range(10)]
print(lst)
sorted_list = bucket_sort(lst)
print(sorted_list)
