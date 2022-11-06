"""1"""
data_list = [lambda x: x + i for i in range(10)]  # [函数,函数,函数]   i=9

v1 = data_list[0](100)
v2 = data_list[3](100)
print(v1, v2)  # 109 109

"""2"""


def num():
    return [lambda x: i * x for i in range(4)]


# 1. num()并获取返回值  [函数,函数,函数,函数] i=3
# 2. for循环返回值
# 3. 返回值的每个元素(2)
result = [m(2) for m in num()]  # [6,6,6,6]
print(result)

"""3"""


def num():
    return (lambda x: i * x for i in range(4))


# 1. num()并获取返回值  生成器对象
# 2. for循环返回值
# 3. 返回值的每个元素(2)
result = [m(2) for m in num()]  # [0,2,4,6]
print(result)
