"""钢条切割问题"""


def cut_recurision(li, n):
    """
    递归方式一
    """
    if n == 0:
        return 0
    else:
        res = li[n]
        for i in range(1, n):
            res = max(res, cut_recurision(li, i) + cut_recurision(li, n - i))
        return res


def cut_recurision_2(li, n):
    """
    递归方式二
    """
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, li[i] + cut_recurision_2(li, n - i))
        return res


def cut_no_recurision(li, n):
    """非递归方式（速度快）"""
    tmp_list = [0, ]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, li[j] + tmp_list[i - j])
        tmp_list.append(res)
    return tmp_list[n]


def cut_no_recurision_extend(li, n):
    r_list = [0, ]
    s_list = [0, ]
    for i in range(1, n + 1):
        r = 0  # 价格的最大值
        s = 0  # 价格最大值对应方案的左边不切割部分的长度
        for j in range(1, i + 1):
            if li[j] + r_list[i - j] > r:
                r = li[j] + r_list[i - j]
                s = j
        r_list.append(r)
        s_list.append(s)
    return r_list[n], s_list


def cut_solution(li, n):
    """输出切割方案"""
    r, s = cut_no_recurision_extend(li, n)
    print(r, s)
    res = []
    while n > 0:
        res.append(s[n])
        n -= s[n]
    return res


if __name__ == '__main__':
    li = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
    # li = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    # print(cut_recurision(li, 15))
    # print(cut_recurision_2(li, 15))
    # print(cut_no_recurision(li, 15))
    # print(cut_no_recurision_extend(li, 15))
    print(cut_solution(li, 20))
