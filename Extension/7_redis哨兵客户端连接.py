import redis
from redis.sentinel import Sentinel

# 连接哨兵服务器
# 10.0.0.10:26379
sentinel = Sentinel(
    [
        ('10.0.0.10', 26379),
        ('10.0.0.10', 26378),
        ('10.0.0.10', 26377)
    ],
    socket_timeout=5
)

print(sentinel)

# 获取主服务器地址
master = sentinel.discover_master('mymaster')
print(master)

# 获取从服务器地址
slave = sentinel.discover_slaves('mymaster')
print(slave)

# 读写分离
# 获取主服务器进行写入
master = sentinel.master_for('mymaster', password='root123456', db=0, socket_timeout=0.5)
w_ret = master.set('like', 'girl')
# 获取从服务器进行读操作
slave = sentinel.slave_for('mymaster', password='root123456', db=0, socket_timeout=0.5)
r_ret = slave.get('like')
print(r_ret)
