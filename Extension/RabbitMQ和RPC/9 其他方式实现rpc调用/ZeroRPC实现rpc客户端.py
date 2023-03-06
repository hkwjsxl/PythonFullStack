import zerorpc
import time


def zerorpc_client():
    print('zerorpc client')
    c = zerorpc.Client()
    c.connect('tcp://127.0.0.1:4243')
    data = {'client:' + str(i): i for i in range(100)}
    start = time.time()
    for i in range(500):
        a = c.getObj()
        print(a)
    for i in range(500):
        c.sendObj(data)

    print('total time %s' % (time.time() - start))


if __name__ == '__main__':
    zerorpc_client()
