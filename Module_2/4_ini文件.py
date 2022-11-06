from configparser import ConfigParser

config = ConfigParser()
config.read(r'file\my.conf', 'utf-8')

# 获取所有节点
option = config.sections()
print(option)  # ['mysqld', 'mysqld_safe', 'client']

# 获取节点下的键值
result = config.items('mysqld_safe')
print(result)
for k, v in result:
    print(k, v)

# 获取节点下的键对应的值
result = config.get('mysqld_safe', 'log-error')
print(result)

# 判断节点是否存在
result = config.has_section('mysqld')
print(result)
# 判断节点的键是否存在
result = config.has_option('mysqld_safe', 'log-error')
print(result)

# 新增节点
# config.add_section('user')  # 只是在内存，section存在会报错
# config.set('user', 'name', 'hkw')
# config.set('user', 'age', '18')
# config.write(open(r'file\my.conf', 'w', encoding='utf-8'))  # 源文件
# config.write(open(r'file\my_new.conf', 'w', encoding='utf-8'))  # 新文件

# 删除节点
# config.remove_section('user')
# config.remove_option('user', 'age')
# config.write(open(r'file\my.conf', 'w', encoding='utf-8'))  # 源文件


