"""
客户端：
	1. 运行程序，连接服务端并获取服务端发送的欢迎使用xx系统信息。
    2. 输入用户名和密码，并将用户名和密码发送到服务端去校验。
    3. 登录失败，重试（Q退出）。
    4. 登录成功，进入系统，提示登录成功
"""

from socket import socket
import json

client = socket()
client.connect(('127.0.0.1', 6789))

server_data = client.recv(1024)
print(server_data.decode('utf-8'))

while True:
    user = input('user:>>>').strip()
    pwd = input('pwd:>>>').strip()
    user_info = f'{user}|{pwd}'
    client.sendall(user_info.encode('utf-8'))

    server_data = client.recv(1024)
    server_data = json.loads(server_data.decode('utf-8'))
    print(server_data['code'], server_data['message'])
    if server_data['code'] == 200:
        break

client.close()
