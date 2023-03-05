# 误判率测试
import redis

client = redis.Redis(host='10.0.0.10', port=6666)
size = 100000
count = 0
client.execute_command("bf.reserve", "hkw", 0.001, size)  # 如果没有这一行，误判率会高很多（error rate: 1.096%）
for i in range(size):
    client.execute_command("bf.add", "hkw", "xxx%d" % i)
    result = client.execute_command("bf.exists", "hkw", "xxx%d" % (i + 1))
    if result == 1:
        print(i)
        count += 1
print("size: {} , error rate: {}%".format(size, round(count / size * 100, 5)))
"""
结果：
85547
91103
93019
size: 100000 , error rate: 0.003%
"""
