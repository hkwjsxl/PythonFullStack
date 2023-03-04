from redis.sentinel import Sentinel

SOCKET_TIMEOUT = 10


class RedisSentinel:
    def __init__(self, sentinel_list, name="mymaster", password="root123456", db=0):
        self.sentinel = Sentinel(sentinel_list, socket_timeout=SOCKET_TIMEOUT)
        self.name = name
        self.password = password
        self.db = db

    def get_master_and_slave_conn(self):
        master = self.sentinel.master_for(
            service_name=self.name,
            socket_timeout=SOCKET_TIMEOUT,
            password=self.password,
            db=self.db)
        slave = self.sentinel.slave_for(
            service_name=self.name,
            socket_timeout=SOCKET_TIMEOUT,
            password=self.password,
            db=self.db
        )
        return master, slave


redis_sentinel = RedisSentinel(
    [
        ('10.0.0.10', 26379),
        ('10.0.0.10', 26378),
        ('10.0.0.10', 26377)
    ]
)
master, slave = redis_sentinel.get_master_and_slave_conn()

w_ret = master.set('program', 'python')
r_ret = slave.get('program')
print(r_ret)
