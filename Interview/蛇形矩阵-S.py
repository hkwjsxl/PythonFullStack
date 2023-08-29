"""

输入：3
输出：
[
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 9]
]

4
[
    [1, 2, 3, 4],
    [8, 7, 6, 5],
    [9, 10, 11, 12],
    [16, 15, 14, 13]
]
"""


def snake_matrix(n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    num = 1
    for i in range(n):
        if i % 2 == 0:
            # 顺序
            for j in range(n):
                matrix[i][j] = num
                num += 1
        else:
            # 逆序
            for j in range(n - 1, -1, -1):
                matrix[i][j] = num
                num += 1
    return matrix


if __name__ == '__main__':
    print(snake_matrix(4))
