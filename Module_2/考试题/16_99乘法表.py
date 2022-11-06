"""基于列表推导式一行实现输出9*9乘法表。"""

"""
# 
# 第一步：[['{}*{}'.format(i, j) for j in range(1, i + 1)] for i in range(1, 10)]
# 第二步：[" ".join(['{}*{}'.format(i, j) for j in range(1, i + 1)]) for i in range(1, 10)]
# 第三步：'\n'.join([" ".join(['{}*{}'.format(i, j) for j in range(1, i + 1)]) for i in range(1, 10)])
"""


def run():
    result = '\n'.join([''.join(['{} * {} = {} '.format(i, j, i * j) for j in range(1, i + 1)]) for i in range(1, 10)])
    print(result)


if __name__ == '__main__':
    run()
