import socket
from utils import req

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9000))

req.send_data(client, "login alex 123")
reply = req.recv_data(client)
print(reply.decode("utf-8"))

req.send_data(client, "upload v1.txt")
reply = req.recv_data(client)
print(reply.decode("utf-8"))

# 开始上传文件
req.send_file(client, 'wupeiqi.txt')

reply = req.recv_data(client)
print(reply.decode("utf-8"))

req.send_data(client, "q")
client.close()
