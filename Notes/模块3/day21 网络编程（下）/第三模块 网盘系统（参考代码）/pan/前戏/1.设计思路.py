class PanHandler(object):
    """ 业务功能代码 """

    def execute(self):
        pass


class Server(object):
    """ 基于普通socket的服务端 """

    def run(self, handler_class):
        # socket服务端
        # 一旦接受到请求之后，就让他执行 PanHandler
        instance = handler_class()
        instance.execute()
        pass


class SelectServer(object):
    """ 基于IO多路复用的socket的服务端 """

    def run(self, handler_class):
        # socket服务端(IO多路复用）
        # 一旦接受到请求之后，就让他执行 PanHandler
        instance = handler_class()
        instance.execute()
        pass


if __name__ == '__main__':
    server = Server()
    # server = SelectServer()
    server.run(PanHandler)
