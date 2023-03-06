import time
from xmlrpc.client import ServerProxy


# SimpleXMLRPCServer
def xmlrpc_client():
    print('xmlrpc client')
    c = ServerProxy('http://localhost:4242')
    data = {'client:' + str(i): i for i in range(100)}
    start = time.time()
    for i in range(10):
        a = c.getObj()
        print(a)
    for i in range(10):
        c.sendObj(data)
    print('xmlrpc total time %s' % (time.time() - start))


if __name__ == '__main__':
    xmlrpc_client()
