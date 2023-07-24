"""斐波那契"""


def fibonacci(n=20):
    """递归版本（非常慢）"""
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_no_recursion(n=20):
    """非递归版本（更快）"""
    tmp_list = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            tmp_list.append(tmp_list[-1] + tmp_list[-2])
        return tmp_list[n]
    return tmp_list[n]


if __name__ == '__main__':
    # print(fibonacci())
    print(fibonacci_no_recursion())
