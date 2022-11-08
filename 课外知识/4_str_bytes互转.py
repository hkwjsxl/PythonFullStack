data = 'hello world 激昂'

# 字符串转二进制
data = bytes(data, encoding='utf-8')
print(data)

# 二进制转字符串
data = str(data, encoding='utf-8')
print(data)
