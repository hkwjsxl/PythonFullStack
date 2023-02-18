import time
import requests
import requests_cache

# 使用默认的sqlite数据库
# requests_cache.install_cache('req_cache')
# 使用文件夹
# requests_cache.install_cache('req_cache', backend='filesystem')
# 使用系统临时文件文件夹，不会在代码区生成
requests_cache.install_cache('req_cache', backend='filesystem', use_temp=True)
# 使用另外的数据库
# backend = requests_cache.RedisCache(host='localhost', port=6379)
# requests_cache.install_cache('req_cache', backend=backend)

start = time.time()
session = requests.Session()
for i in range(10):
    session.get('http://httpbin.org/delay/1')
    print(f'Finished {i + 1} requests')
end = time.time()
print('Cost time', end - start)
