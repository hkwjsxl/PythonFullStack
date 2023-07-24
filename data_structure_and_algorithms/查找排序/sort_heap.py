"""堆排序"""

import random


def sift(lst, low, high):
    """
    堆的向下编排函数（大根堆），每一次编排让堆变得有序
    :param lst: 列表
    :param low: 堆顶（堆的根位置）
    :param high: 堆尾（堆的最后一个位置）
    :return:
    """
    i = low  # i首先表示第一行
    j = 2 * i + 1  # j表示i的左节点
    tmp = lst[low]  # 拿到此时的堆顶
    while j <= high:  # 确保左节点有值
        if j + 1 <= high and lst[j] < lst[j + 1]:  # 判断左右孩子节点哪个大，并且j+1也就是右节点没有越出堆的底部
            j += 1  # 如果右节点大，则j指向右节点
        if tmp < lst[j]:  # 如果拿到的值比堆下面的值小，就让下面的比较大的值上来
            lst[i] = lst[j]  # 下面的值上去
            i = j  # i和j往下一层
            j = 2 * i + 1
        else:
            lst[i] = tmp  # 如果拿到的值比下面的值大，表示不用替换，堆已经形成，并且结束循环
            break
    else:
        lst[i] = tmp  # 没有左节点


def heap_sort(lst):
    n = len(lst)
    # 建堆
    for i in range(n // 2 - 1, -1, -1):  # i表示每次建堆的根节点的下标
        sift(lst, i, n - 1)
    # 出数
    for i in range(n - 1, -1, -1):  # i指向当前堆的最后一个元素
        lst[0], lst[i] = lst[i], lst[0]  # 将最大的元素依次放到堆尾
        sift(lst, 0, i - 1)  # 进行一次堆编排调整使得堆有序，i-1是新的high，此前的high的位置存放当前最大值


lst = [random.randrange(10, 99) for i in range(10)]
print(lst)
heap_sort(lst)
print(lst)
