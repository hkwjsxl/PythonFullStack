"""最长公共子序列"""


def lcs_length(x, y):
    """返回最长公共子序列的长度"""
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                # i,j位置上的字符匹配时，当前位置的数值来源于左上角的数值加1
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                # i,j位置上的字符不匹配时，当前位置的数值来源于 左方或上方的最大数值
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]


def lcs(x, y):
    """标出最长公共子序列的匹配箭头"""
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 标出箭头
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                # 匹配用左上方箭头，数字1表示
                c[i][j] = c[i - 1][j - 1] + 1
                d[i][j] = 1
            elif c[i - 1][j] > c[i][j - 1]:
                # 来源于上方，数字2表示
                c[i][j] = c[i - 1][j]
                d[i][j] = 2
            else:
                # 来源于左边，数字3表示
                c[i][j] = c[i][j - 1]
                d[i][j] = 3
    return c[m][n], d


def lcs_back(x, y):
    """回溯，生成最长公共子序列字符串"""
    i = len(x)
    j = len(y)
    length, d = lcs(x, y)
    tmp_list = []
    while i > 0 and j > 0:
        if d[i][j] == 1:
            # 左上方的箭头(两个字符匹配时)
            tmp_list.append(x[i - 1])
            i -= 1
            j -= 1
        elif d[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(tmp_list))


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    print(lcs_length(x, y))
    print("".center(50, "-"))

    c, d = lcs(x, y)
    for line in d:
        print(line)
    print("".center(50, "-"))

    print(lcs_back(x, y))
