# 1.简述面向对象的三大特性
"""
封装
    把多个数据封装到一个类中，多个方法封装到一个类型中
继承
    把多个子类的方法封装到父类中，子类可调用父类的方法，提供代码的重用性
多态
    本身支持多态，提倡鸭子类型，不会对类型进行限制，只要具备相同的属性即可
"""

# 2.super的作用？
"""向上层查找父类的方法或数据，在重写父类方法时保留父类的功能"""

# 3.实例变量和类变量的区别？
"""
实例变量属于对象
类变量属于类
"""

# 4.@staticmethod 和 @classmethod的区别？
"""
两者都不用写self参数，都可以不用实例化调用方法（类.方法()）

前者静态方法，可以不传参数，类似于普通函数
后者是类方法，默认有cls参数，cls是当前调用的对象本身
"""

# 5.简述 `__new__`和`__init__`的区别？
"""
前者是构造方法，构造类时触发，在初始化方法之前
后者是初始化方法
"""

# 6.在Python中如何定义私有成员？
"""成员前加__"""

# 7.请基于`__new__` 实现一个单例类（加锁）。
"""
from threading import RLock

class Singleton:
    instance = None
    rlock = RLock()
    
    def __init__(self):
        pass
        
    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
            
        with cls.rlock:
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
        return cls.instance
        
"""

# 8.一个调用F1一个调用F2

# 9
"""
class Context:
    pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def do_something(self):
        print('do')


with Context() as ctx:
    ctx.do_something()

"""

# 10.简述 迭代器、可迭代对象 的区别？
"""
迭代器：内部有iter和next方法，iter返回对象本身，next是下一次要取出的内容，超出则抛出Stopiteration的错误
可迭代对象：内部有iter方法，但没有next方法，可以for循环取值，iter方法返回迭代器对象
"""
# 11.什么是反射？反射的作用？
"""
定义：基于字符串的形式方便的操作类的成员
作用：方便的操作类的成员
"""
# 12.简述OSI七层模型。
"""
应用层，表示层，会话层，传输层，网络层，数据链路层，物理层
规定数据的格式
    对数据进行封装，拆分，解压缩，加解密，对会话的两端进行连接
        建立会话
            建立端到端的连接
                网络管理，标记ip
                    设置MAC地址信息
                        将二进制数据在物理媒介上传输
                    
每一层都有对应的功能，可在需要时对里面的数据进行操作

"""
# 13.UDP和TCP的区别。
"""
前者是不可靠的协议，在不要求通话质量时使用，比如音视频
后者是可靠的的协议，要求数据收发时必须先建立连接，以此保证通话的质量
"""
# 14.简述TCP三次握手和四次挥手的过程。
"""
客户端给服务端发消息说我要给你发消息
服务端回复，可以发，并且向客户端发送消息
客户端接收到服务端的回复，并开始发送消息

客户端说我要结束通话
服务端接收到可以，并说稍等一下
服务端说可以了
客户端说好的，并结束
"""
# 15.简述你理解的IP和子网掩码。
"""
IP：固定的32位二进制数据
子网掩码：对ip的划分，分为网络地址和主机地址
"""
# 16.端口的作用？
"""
ip标记计算机，端口标记计算机上的某个应用或程序
"""
# 17.什么是粘包？如何解决粘包？
"""
客户端向服务端发送数据时，服务端由于网络或其他原因，接收较慢，这时如果客户端发送多次数据并速度较快，数据会粘连到一起发送过去

每一次发送数据前前把本次要发送的数据的长度按照固定的位数发过去，另一方在接收时先把本次数据长度按照固定的位数取出来，再接收数据
"""
# 18.IO多路复用的作用是什么？
"""
使得服务端可以接收并回复多个客户端发来的信息
"""
# 19.简述进程、线程、协程的区别。
"""
进程：计算机分配资源的最小单位，进程之间数据不共享
线程：计算机的cpu所能调用的最小单位，同一进程下的线程之间数据共享
协程：让cpu不间歇的在多个任务中切换，极大的提高了执行效率
"""
# 20.什么是GIL锁？其作用是什么？
"""
全局解释器锁，Cpython所特有的，让cpu在同一时刻只能调用一个线程，降低了效率，但保证了数据安全
"""
# 21.进程之间如何实现数据的共享？
"""
队列，管道
Queqe，Piple
"""
# 22.
# import json
#
#
# class JsonEncoder(json.JSONEncoder):
#     def default(self, o):
#         if type(o) in (TradeOrder, Shop):
#             return o.__dict__
#         return o
#
#
# class TradeOrder:
#     def __init__(self, nid, name, items, is_member):
#         """
#         :param nid: ID(int)
#         :param name: 姓名(str)
#         :param items: 商品类型(list)
#         :param is_member: 是否是会员(bool)
#         """
#         self.nid = nid
#         self.name = name
#         self.items = items
#         self.is_member = is_member
#
#     def add_shop(self, *args):
#         for obj in args:
#             self.items.append(obj)
#
#
# class Shop:
#     def __init__(self, nid, name):
#         """
#         :param nid: 主键(int)
#         :param name: 商品名称(str)
#         """
#         self.nid = nid
#         self.name = name
#
#
# if __name__ == '__main__':
#     t1 = TradeOrder(1, 'hkw', [], True)
#     s1 = Shop(1, '手机')
#     s2 = Shop(2, '平板')
#
#     t1.add_shop(s1, s2)
#     data = json.dumps(t1, cls=JsonEncoder)
#     print(data)


# 23.
"""
class Node:
    def __init__(self, value, _next):
        self.value = value
        self._next = _next


data_list = ["alex", "武沛齐", "女神", "火蜥蜴"]
root = None
for i in range(len(data_list) - 1, -1, -1):
    n = Node(data_list[i], root)
    root = n
    print(n.value)

"""


