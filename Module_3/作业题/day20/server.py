"""
服务端：
	1. 客户端连接上服务端，返回 欢迎使用xx系统信息。
    2. 等待客户端发送用户名和密码进行校验（用户名和密码在文件中）
    3. 登录失败，返回错误信息。
    4. 登录成功，返回成功提示的内容。
"""

from socket import socket
import json

server = socket()
server.bind(('127.0.0.1', 6789))
server.listen(5)

while True:
    conn, addr = server.accept()
    conn.sendall('欢迎啊！'.encode('utf-8'))
    while True:
        client_data = conn.recv(1024)
        print(client_data)
        if not client_data:
            break
        client_data = client_data.decode('utf-8')
        user, pwd = client_data.split('|')
        userinfo_dict = {'code': 200, 'message': '登陆成功！'}
        with open('user_info.csv', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                username, password = line.split(',')
                if user == username and pwd == password:
                    conn.sendall(json.dumps(userinfo_dict).encode('utf-8'))
                    break
            else:
                userinfo_dict['code'] = 400
                userinfo_dict['message'] = '登录失败！'
                conn.sendall(json.dumps(userinfo_dict).encode('utf-8'))
    conn.close()

server.close()
