"""最大公约数---欧几里得算法"""


def gcd(a, b):
    """递归求法"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_no_recursion(a, b):
    """非递归求法"""
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a


if __name__ == '__main__':
    print(gcd(12, 16))
    print(gcd_no_recursion(12, 16))
