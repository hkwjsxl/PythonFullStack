"""
- 客户端
  - 用户注册，注册成功之后，在服务端的指定目录下为此用户创建一个文件夹，该文件夹下以后存储当前用户的数据（类似于网盘）。
  - 用户登录
  - 查看网盘目录下的所有文件（一级即可），ls命令
  - 上传文件，如果网盘已存在则重新上传（覆盖）。
  - 下载文件（进度条）
      先判断要下载本地路径中是否存在该文件。
          - 不存在，直接下载
          - 存在，则让用户选择是否续传（继续下载）。
	          - 续传，在上次的基础上继续下载。
	          - 不续传，从头开始下载。
"""
import os
import socket
import json
import time
from datetime import datetime

from tqdm import tqdm

import setting
from utils import send_data, recv_data, send_file, client_recv_file


class Client:
    def __init__(self):
        self.ip = setting.IP
        self.port = setting.PORT
        self.client = socket.socket()
        self.client.connect((self.ip, self.port))
        self.is_login = False
        self.login_info = {'is_login': False, 'username': ''}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            send_data(self.client, 'close')
            self.client.close()

    # def login_auth(self, func):
    #     @wraps(func)
    #     def inner(*args, **kwargs):
    #         if not self.is_login:
    #             self.login()
    #         res = func(*args, **kwargs)
    #         return res
    #
    #     return inner

    def run(self):
        # 提示信息
        print('网盘系统'.center(50, '-'))
        option_dict = {
            '1': ('注册', self.register),
            '2': ('登录', self.login),
            '3': ('上传文件', self.upload_file),
            '4': ('下载文件', self.download_file),
            '5': ('查看目录', self.look_dir),
        }
        for index, option in option_dict.items():
            print(index, option[0])
        while True:
            # 发送功能序号
            choice = input('请输入要执行的功能(Q退出)>>>').strip()
            if choice.upper() == 'Q':
                send_data(self.client, 'close')
                break
            if not choice.isdecimal():
                print('序号输入不合法!')
                continue
            choice = int(choice)
            if choice < 1 or choice > len(option_dict):
                print('序号输入不正确!')
                continue
            choice = str(choice)
            send_data(self.client, choice)
            res_msg = option_dict[choice][1]()
            if res_msg:
                print(res_msg)

    def register(self):
        print('注册'.center(50, '-'))
        username = input('username:>>>').strip()
        passwrod = input('passwrod:>>>').strip()
        user_info = {
            '1': username,
            '2': passwrod,
            '3': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        send_data(self.client, json.dumps(user_info))
        res_data = recv_data(self.client)
        res_data = json.loads(res_data)
        print(res_data)

    def login(self):
        print('登录'.center(50, '-'))
        username = input('username:>>>').strip()
        passwrod = input('passwrod:>>>').strip()
        user_info = {
            'username': username,
            'password': passwrod,
        }
        send_data(self.client, json.dumps(user_info))
        res_data = recv_data(self.client)
        res_data = json.loads(res_data)
        print(res_data)
        if res_data.get('code') == 200:
            self.login_info['is_login'] = True
            self.login_info['username'] = username

    def upload_file(self):
        if not self.login_info['is_login']:
            send_data(self.client, 'continue')
            return '请先登录'

        print('上传文件'.center(50, '-'))
        while True:
            try:
                file_path = input('请输入要上传文件的路径(Q退出)>>>').strip().strip('\"')
                if file_path.upper() == 'Q':
                    break
                if not os.path.exists(file_path):
                    print('文件路径不存在!')
                    continue
                file_name = file_path.rsplit(os.sep, maxsplit=1)[-1]
                # 网盘文件路径
                file_name = os.path.join(self.login_info.get('username'), file_name)
                send_data(self.client, file_name)
                send_file(self.client, file_path)

                res_data = recv_data(self.client)
                res_data = json.loads(res_data)
                print(res_data)
                break
            except Exception as e:
                print(f'上传失败!---{e}')
                send_data(self.client, 'close')
                break

    def download_file(self):
        if not self.login_info['is_login']:
            send_data(self.client, 'continue')
            return '请先登录'

        print('下载文件'.center(50, '-'))
        while True:
            file_name = input('请输入要下载的文件名(Q退出)>>>').strip().strip('\"')
            if file_name.upper() == 'Q':
                break

            # 网盘文件路径
            wp_file_name = os.path.join(self.login_info.get('username'), file_name)
            # 文件是否在本地存在
            if not os.path.exists(file_name):
                send_data(self.client, wp_file_name)

                res_data = recv_data(self.client)
                res_data = json.loads(res_data)
                print(res_data)
                if res_data.get('code') == 400:
                    send_data(self.client, 'continue')
                    break
                else:
                    client_recv_file(self.client, file_name)
                    res_data = recv_data(self.client)
                    res_data = json.loads(res_data)
                    self.jindutiao()
                    print(res_data)
            else:
                # 断点续传
                is_con = input('是否断点续传(Y/N)>>>').strip()
                if is_con.upper() not in ['Y', 'N']:
                    print('输入错误!')
                    send_data(self.client, 'continue')
                    break
                if is_con.upper() == 'Y':
                    print('Y')
                    # 当前文件seek
                    file_seek = os.stat(file_name).st_size
                    send_data(self.client, wp_file_name, file_seek)

                    res_data = recv_data(self.client)
                    res_data = json.loads(res_data)
                    print(res_data)
                    if res_data.get('code') == 400:
                        send_data(self.client, 'continue')
                        break
                    else:
                        client_recv_file(self.client, file_name)
                        res_data = recv_data(self.client)
                        res_data = json.loads(res_data)
                        self.jindutiao()
                        print(res_data)
                else:
                    print('N')
                    send_data(self.client, wp_file_name)

                    res_data = recv_data(self.client)
                    res_data = json.loads(res_data)
                    print(res_data)
                    if res_data.get('code') == 400:
                        send_data(self.client, 'continue')
                        break
                    else:
                        client_recv_file(self.client, file_name)
                        res_data = recv_data(self.client)
                        res_data = json.loads(res_data)
                        self.jindutiao()
                        print(res_data)
                    break
            break

    def jindutiao(self):
        for i in tqdm(range(100)):
            time.sleep(0.02)

    def look_dir(self):
        if not self.login_info['is_login']:
            send_data(self.client, 'continue')
            return '请先登录'

        print('查看目录'.center(50, '-'))
        send_data(self.client, 'ls')
        send_data(self.client, self.login_info['username'])

        res_data = recv_data(self.client)
        if not res_data:
            send_data(self.client, 'continue')
            return '内部错误!'
        res_data = json.loads(res_data)
        print(f'目录文件列表---{res_data["data"]}')


if __name__ == '__main__':
    with Client() as client_obj:
        client_obj.run()
