"""青蛙跳阶问题"""


def frog_jump(n=10):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007


if __name__ == '__main__':
    print(frog_jump())
