from xmlrpc.server import SimpleXMLRPCServer


class RPCServer(object):

    def __init__(self):
        super(RPCServer, self).__init__()
        print('self', self)
        self.send_data = {'server:' + str(i): i for i in range(100)}
        self.recv_data = None

    def getObj(self):
        print('get data')
        return self.send_data

    def sendObj(self, data):
        print('send data')
        self.recv_data = data
        print(self.recv_data)


# SimpleXMLRPCServer
server = SimpleXMLRPCServer(('localhost', 4242), allow_none=True)
server.register_introspection_functions()
server.register_instance(RPCServer())
server.serve_forever()
