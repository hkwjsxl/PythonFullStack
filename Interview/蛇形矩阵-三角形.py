"""
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11

"""


def func(n):
    res = []
    for i in range(n):
        if i == 0:
            # 第一行
            for e in range(n):
                res.append((e + 1) * (e + 2) // 2)
        else:
            # 后面几行，是前一行去掉第一个元素后，前一行元素减一
            res = [e - 1 for e in res[1:]]
        print(' '.join(map(str, res)))


if __name__ == '__main__':
    func(5)
