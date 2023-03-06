import zerorpc


class RPCServer(object):

    def __init__(self):
        super(RPCServer, self).__init__()
        self.send_data = {'server:' + str(i): i for i in range(100)}
        self.recv_data = None

    def getObj(self):
        print('get data')
        return self.send_data

    def sendObj(self, data):
        print('send data')
        self.recv_data = data
        print(self.recv_data)


s = zerorpc.Server(RPCServer())
s.bind('tcp://0.0.0.0:4243')
s.run()
