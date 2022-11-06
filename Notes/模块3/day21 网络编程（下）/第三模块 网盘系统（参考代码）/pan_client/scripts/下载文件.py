import os
import json
import socket
from utils import req

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9000))

req.send_data(client, "login alex 123")
reply = req.recv_data(client)
print(reply.decode("utf-8"))

# #### 本地检测 ####
local_path = '顺丰快递.txt'
seek = 0
if os.path.exists(local_path):
    seek = os.stat(local_path).st_size
    print(seek)
    req.send_data(client, "download 顺丰快递.txt {}".format(seek))
    mode = 'ab'
else:
    req.send_data(client, "download 顺丰快递.txt")
    mode = 'wb'

# 获取返回值
reply = req.recv_data(client).decode('utf-8')
reply_dict = json.loads(reply)
if not reply_dict['status']:
    print(reply_dict['error'])
else:
    print(reply_dict['data'])
    req.recv_save_file_with_progress(client, local_path, mode, seek=seek)
    print("下载完毕")

req.send_data(client, "q")
client.close()
