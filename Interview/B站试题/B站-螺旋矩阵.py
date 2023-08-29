"""
螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素
时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 256M，其他语言512M
示例1
输入例子：
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
输出例子：
[1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def SpiralMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix[0]
            matrix = list(zip(*matrix[1:]))[::-1]
            # print(matrix)
        return res


ret = Solution().SpiralMatrix(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [66, 77, 88, 99],
    ]
)
print(ret)
