import socket
import select


class PanHandler(object):
    """ 业务功能代码 """

    def __init__(self, conn):
        self.conn = conn

    def execute(self):
        """
        处理客户端的请求
        :return:  False，断开连接；True，继续执行当前客户端发来的请求。
        """
        data = self.conn.recv(1024)

        content = data.decode('utf-8')

        if content.upper() == "Q":
            return False

        # 1.处理登录
        # "login wupeiqi xxx"

        # 2.注册
        # register wupeiqi xxx

        # ....

        self.conn.sendall(b'xxxx')

        return True


class Server(object):
    """ 基于普通socket的服务端 """

    def run(self, handler_class):
        # socket服务端
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("IP", "端口"))
        sock.listen(5)

        while True:
            # 等待，客户端发来连接
            conn, addr = sock.accept()

            # 新客户端到来。 PanHandler对象
            instance = handler_class(conn)
            # 处理客户端的请求。 PanHandler对象.execute
            while True:
                result = instance.execute()
                if not result:
                    break

            conn.close()

        sock.close()


class SelectServer(object):
    """ 基于IO多路复用的socket的服务端 """

    def run(self, handler_class):
        server_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_object.setblocking(False)
        server_object.bind(("IP", "端口"))
        server_object.listen(5)


        socket_object_list = [server_object, "客户端socket对象1","客户端socket对象2" ]


        conn_handler_map = {
            "客户端socket对象1": PanHandler(conn1),
            "客户端socket对象2": PanHandler(conn2),
        }

        while True:

            # r = ["客户端socket对象4", ]
            r, w, e = select.select(socket_object_list, [], [], 0.05)

            for sock in r:
                # sock="客户端socket对象4"

                # 新连接到来，执行 handler的 __init__ 方法
                if sock == server_object:
                    print("新客户端来连接")
                    conn, addr = server_object.accept()
                    socket_object_list.append(conn)
                    # 实例化handler类，即：类(conn)
                    conn_handler_map[conn] = handler_class(conn)
                    continue

                # 一旦有请求发来，找到相关的 handler对象，执行他的 execute方法。
                #  execute方法返回False，则意味着此客户端要断开连接。
                handler_object = conn_handler_map[sock]   # 自己PanHandler(conn1),

                # 找到execute去处理各自的业务逻辑
                result = handler_object.execute()
                if not result:
                    socket_object_list.remove(sock)
                    del conn_handler_map[sock]

        sock.close()


if __name__ == '__main__':
    # server = Server()
    server = SelectServer()
    server.run(PanHandler)
