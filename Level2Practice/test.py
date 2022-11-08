import random
import time
import keyword


def main():
    # print(divmod(10, 3))
    # print(pow(3, 3))
    # print(round(2.44, 1))
    # print(ord('A'))
    # print(chr(65))
    # print(hex(15))
    # print(hex(16))
    # print(hex(17))
    # print('123456789'.find('1'))
    # print(float('123.456'))
    # l = [1, 5, 2, 3]
    # l.sort()
    # print(l)
    # print(l.count(1))
    # dic = {
    #     'name': 'hkw',
    #     'age': '18'
    # }
    # s = ('google', 'baidu')
    # d = dic.fromkeys(s, '1')
    # print(d)
    # print(dic.popitem())
    #
    # random.seed(1)  # 传入的数值用于指定随机数生成时所用算法开始时所选定的整数值，如果使用相同的seed()值，则每次生成的随机数都相同
    # print(random.randint(1, 2))
    # print(random.randint(1, 2))
    # print(random.getrandbits(123))
    # print(random.uniform(1, 2))
    # print(random.sample([1, 2, 3], 2))

    # print(time.gmtime())
    # print(time.localtime())
    # print(time.ctime())
    # print(time.strftime('%z', time.localtime()))
    # print(time.perf_counter())
    # print(1)

    # s = 'hello world'
    # print(s.title())
    # print(s.capitalize())
    # ss = 'a1b2c345'
    # i = j = 0
    # for line in ss:
    #     if line.isnumeric():
    #         i += 1
    #     if line.isalpha():
    #         j += 1
    # print(i, j)

    # l = [1,2]
    # l.reverse()
    # print(l)

    """输出当年的日历"""
    # import calendar
    #
    # year = 2022
    # t = calendar.calendar(year)
    # print(t)

    """太阳花"""
    # import turtle
    # turtle.color('red', 'yellow')
    # turtle.begin_fill()
    # for i in range(36):
    #     turtle.fd(200)
    #     turtle.left(170)
    # turtle.end_fill()
    # time.sleep(5)

    # n = input('请输入一个正整数:')
    # for i in range(int(n)):
    #     print('{:0>2} {}'.format(i + 1, ">" * (i + 1)))

    # print('{:=>5}'.format(123))

    # x = eval(input('>>>'))
    # print("{:c}".format(x))

    # s = input('>>>')
    # print("{:\"^30x}".format(eval(s)))

    # print('@'.center(10, '-'))
    # print('0b{0:b},0o{0:o},0x{0:x}'.format(10))

    # s = '123'
    # print(s[::-1])
    # print('{:\"^10x}'.format(eval('16')))
    ...


if __name__ == '__main__':
    # print(keyword.kwlist)  # 内置函数
    main()
