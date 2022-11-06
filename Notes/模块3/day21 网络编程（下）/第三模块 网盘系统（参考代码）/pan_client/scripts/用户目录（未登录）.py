import socket
from utils import req

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9000))

req.send_data(client, "look")
reply = req.recv_data(client)
print(reply.decode("utf-8"))

req.send_data(client, "look xxx")
reply = req.recv_data(client)
print(reply.decode("utf-8"))

req.send_data(client, "look x1")
reply = req.recv_data(client)
print(reply.decode("utf-8"))

req.send_data(client, "look readme")
reply = req.recv_data(client)
print(reply.decode("utf-8"))

req.send_data(client, "q")
client.close()
