"""
编写算法， 将自然数 1～n^2 按“ 蛇形” 填入 n× n 矩阵中。例如

n=4时，自然数1～4^2 填入4 x 4矩阵后：
1	12	11	10
2	13	16	9
3	14	15	8
4	5	6	7

"""


class Solution:
    def print_snake_matrix(self, n: int):
        # 创建一个空的 n x n 矩阵
        matrix = [[0] * n for _ in range(n)]
        # 最大值
        max_num = n ** 2
        # 当前值
        matrix[0][0] = temp_num = 1
        i = j = 0
        # 值未填满
        while temp_num < max_num:
            # 下
            while i + 1 < n and matrix[i + 1][j] == 0:
                i += 1
                temp_num += 1
                matrix[i][j] = temp_num
            # 右
            while j + 1 < n and matrix[i][j + 1] == 0:
                j += 1
                temp_num += 1
                matrix[i][j] = temp_num
            # 上
            while 0 <= i - 1 < n and matrix[i - 1][j] == 0:
                i -= 1
                temp_num += 1
                matrix[i][j] = temp_num
            # 左
            while 0 <= j - 1 < n and matrix[i][j - 1] == 0:
                j -= 1
                temp_num += 1
                matrix[i][j] = temp_num
            # print(i, j)
            # print(temp_num, max_num)
        return matrix


ret = Solution().print_snake_matrix(4)
print(ret)
