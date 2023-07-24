"""
有n个⾮负整数，将其按照字符串拼接的⽅式拼接为⼀个整数。 如何拼接可以使得得到的整数最⼤？

例：32,94,128,1286,6,71可以拼接除的最⼤整数为 94716321286128（考虑128和1286哪个在前）

"""
from functools import cmp_to_key


def xy_cmp(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    return 0


def number_join(number_str_list):
    number_str_list.sort(key=cmp_to_key(xy_cmp))
    return "".join(number_str_list)


if __name__ == '__main__':
    number_list = [32, 94, 128, 1286, 6, 71]
    number_str_list = list(map(str, number_list))
    last_number = number_join(number_str_list)
    print(last_number)
