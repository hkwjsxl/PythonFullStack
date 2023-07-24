"""堆排序---topk问题"""

import random


def sift(lst, low, high):
    """
    堆的向下编排函数（小根堆）
    :param lst: 列表
    :param low: 堆顶（堆的根位置）
    :param high: 堆尾（堆的最后一个位置）
    :return:
    """
    i = low  # i首先表示第一行
    j = 2 * i + 1  # j表示i的左节点
    tmp = lst[low]  # 拿到此时的堆顶
    while j <= high:  # 确保左节点有值
        if j + 1 <= high and lst[j] > lst[j + 1]:  # 判断左右孩子节点哪个大，并且j+1也就是右节点没有越出堆的底部
            j += 1  # 如果右节点大，则j指向右节点
        if tmp > lst[j]:  # 如果拿到的值比堆下面的值小，就让下面的比较大的值上来
            lst[i] = lst[j]  # 下面的值上去
            i = j  # i和j往下一层
            j = 2 * i + 1
        else:
            lst[i] = tmp  # 如果拿到的值比下面的值大，表示不用替换，堆已经形成，并且结束循环
            break
    else:
        lst[i] = tmp  # 没有左节点


def topk(lst, k):
    """
    :param lst: 列表
    :param num: 要取出的最大的前几数值
    :return:
    """
    head = lst[:k]
    # 建堆
    for i in range(k // 2 - 1, -1, -1):
        sift(head, i, k - 1)
    # 遍历
    for i in range(k - 1, len(lst) - 1):
        if lst[i] > lst[0]:
            lst[0] - lst[i]
            sift(head, 0, k - 1)
    # 出数
    for i in range(k - 1, -1, -1):
        head[0], head[i] = head[i], head[0]
        sift(head, 0, i - 1)

    return head


lst = [random.randrange(10, 99) for i in range(100)]
print(lst)
head_lst = topk(lst, 10)
print(head_lst)
