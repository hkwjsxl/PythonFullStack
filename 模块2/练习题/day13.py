"""4"""
"""
data_list = [11, 22, 33, "alex", 455, 'eirc']

new_data_list = [val for val in data_list if type(val) != str]  # 请在[]中补充代码实现。
print(new_data_list)
# 提示：可以用type判断类型
"""

"""5"""
# data_list = [11, 22, 33, "alex", 455, 'eirc']
#
# new_data_list = [len(val) if type(val) == str else val + 100 for val in data_list]  # 请在[]中补充代码实现。
# print(new_data_list)
# 提示：可以基于三元运算实现
"""6"""
data_list = [
    (1, 'alex', 19),
    (2, '老男', 84),
    (3, '老女', 73)
]
# 请使用推导式将data_list构造生如下格式：
"""
info_dict = {
    1:(1,'alex',19),
    2:(2,'老男',84),
    3:(3,'老女',73)
}
"""
# info_dict = {data[0]: data for data in data_list}
# print(info_dict)

"""7"""
# player = {
#     "武沛齐": ["红桃", 10],
#     "alex": ["红桃", 8],
#     'eric': ["黑桃", 3],
#     'killy': ["梅花", 12],
# }
# sort_dict = [k[-1] for k, v in sorted(player.items(), key=lambda x: x[1][1])]
# print(sort_dict)


"""8"""
"""
int str len oct hex bin ord chr getattr setattr hasattr isinstance issubclass
sorted
sum abs pow round divmod
min max all any
btyes type hash help zip callable
"""

"""9"""


# 1 1 2 3 5 8 13 21 34 55 ...
# def fib(max_count):
#     a, b = 0, 1
#     yield b
#     for i in range(max_count - 1):
#         a, b = b, a + b
#         yield b


def fib(max_count):
    first_val = 1
    second_val = 0
    count = 0
    while count < max_count:
        next_val = first_val + second_val
        first_val = second_val
        second_val = next_val
        yield next_val
        count += 1


count = input("请输入要生成斐波那契数列的个数：")
count = int(count)
fib_generator = fib(count)
for num in fib_generator:
    print(num)

