"""
找零
面值1元、4元、16元、64元共计4种硬币，以及面值1024元的纸币。现在小Y使用1024元的纸币购买了一件价值为N(0<N≤1024)的商品，请问最少他会收到多少硬币
时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 256M，其他语言512M
示例1
输入例子：
200
输出例子：
17
例子说明：
12个64元硬币，3个16元硬币，2个4元硬币

"""


def func(N):
    li = [64, 16, 4, 1]
    li.sort(reverse=True)
    print(li)
    m = [0 for _ in range(len(li))]
    for index, value in enumerate(li):
        m[index] = N // value
        N = N % value
    print(m, N)
    ret = 0
    for val in m:
        ret += val
    print(ret)


if __name__ == '__main__':
    func(1024 - 200)
