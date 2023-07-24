"""
找零问题
假设商店⽼板需要找零n元钱，钱币的⾯额有：100元、50元、 20元、5元、1元，如何找零使得所需钱币的数量最少？
"""


def func(li, n):
    li.sort(reverse=True)
    m = [0 for _ in range(len(li))]
    for index, value in enumerate(li):
        m[index] = n // value
        n = n % value
    return m,n


if __name__ == '__main__':
    li = [100, 50, 20, 5, 1]
    print(func(li, 373))
