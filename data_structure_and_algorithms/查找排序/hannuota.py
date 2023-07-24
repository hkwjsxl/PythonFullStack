"""递归：汉诺塔问题"""


# 目的是将n个圆盘从a经过b移动到c
def hanoi(n, a, b, c):
    if n > 0:
        # 第一步：将n-1个圆盘从a经过c移动到b
        hanoi(n - 1, a, c, b)
        # 第二步：将第n个圆盘从a移动到c
        print("%d: moving from %s to %s." % (n, a, c))
        # 第三步：将n-1个圆盘从b经过a移动到c
        hanoi(n - 1, b, a, c)


hanoi(3, "a", "b", "c")
