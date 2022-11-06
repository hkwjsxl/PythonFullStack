import re
import os
import json
import socket
from config import settings
from utils import req


class Handler(object):
    def __init__(self):
        self.host = settings.HOST
        self.port = settings.PORT
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = None

    def run(self):
        self.conn.connect((self.host, self.port))
        welcome = """
        登录：login 用户名 密码
        注册：register 用户名 密码
        查看：ls 目录
        上传：upload 本地目录 远程目录
        下载：download 本地目录 远程目录 
        """
        print(welcome)

        method_map = {
            "login": self.login,
            "register": self.register,
            "ls": self.ls,
            "upload": self.upload,
            "download": self.download,
        }

        while True:
            hint = "({})>>> ".format(self.username or "未登录")
            text = input(hint).strip()
            if not text:
                print("输入不能为空，请重新输入。")
                continue

            if text.upper() == "Q":
                print("退出")
                req.send_data(self.conn, "q")
                break

            cmd, *args = re.split(r"\s+", text)
            method = method_map.get(cmd)
            if not method:
                print("命令不存在，请重新输入。")
                continue
            method(*args)

        self.conn.close()

    def login(self, *args):
        if len(args) != 2:
            print("格式错误，请重新输入。提示：login 用户名 密码")
            return
        username, password = args
        req.send_data(self.conn, "login {} {}".format(username, password))
        reply = req.recv_data(self.conn).decode('utf-8')
        reply_dict = json.loads(reply)
        if reply_dict['status']:
            self.username = username
            print("登录成功")
            return
        print(reply_dict['error'])

    def register(self, *args):
        if len(args) != 2:
            print("格式错误，请重新输入。提示：register 用户名 密码")
            return
        username, password = args

        req.send_data(self.conn, "register {} {}".format(username, password))
        reply = req.recv_data(self.conn).decode('utf-8')
        reply_dict = json.loads(reply)
        if reply_dict['status']:
            print("注册成功")
            return
        print(reply_dict['error'])

    def ls(self, *args):
        if not self.username:
            print("登录后才允许查看目录")
            return
        if not args:
            cmd = "ls"
        elif len(args) == 1:
            cmd = "ls {}".format(*args)
        else:
            print("格式错误，请重新输入。提示：ls 或 ls 目录 ")
            return

        req.send_data(self.conn, cmd)
        reply = req.recv_data(self.conn).decode('utf-8')
        reply_dict = json.loads(reply)
        if reply_dict['status']:
            print(reply_dict['data'])
            return
        print(reply_dict['error'])

    def upload(self, *args):
        if not self.username:
            print("登录后才允许上传")
            return
        if len(args) != 2:
            print("格式错误，请重新输入。提示：upload 本地目录 远程目录")
            return
        local_file_path, remote_file_path = args
        if not os.path.exists(local_file_path):
            print("文件{}不存在，请重新输入。".format(local_file_path))
            return

        req.send_data(self.conn, "upload {}".format(remote_file_path))
        reply = req.recv_data(self.conn).decode('utf-8')
        reply_dict = json.loads(reply)
        if not reply_dict['status']:
            print(reply_dict['error'])
            return

        print("开始长传")  # reply_dict['data']

        # 开始上传文件
        req.send_file(self.conn, local_file_path)

        print("上传完毕")

    def download(self, *args):
        if not self.username:
            print("登录后才允许下载")
            return
        if len(args) != 2:
            print("格式错误，请重新输入。提示：download 本地目录 远程目录")
            return

        local_file_path, remote_file_path = args
        seek = 0
        if not os.path.exists(local_file_path):
            # download v1.txt
            req.send_data(self.conn, "download {}".format(remote_file_path))
            mode = 'wb'
        else:
            choice = input("是否续传（Y/N) ")
            if choice.upper() == 'Y':
                # download v1.txt 100
                seek = os.stat(local_file_path).st_size
                req.send_data(self.conn, "download {} {}".format(remote_file_path, seek))
                mode = 'ab'
            else:
                # download v1.txt
                req.send_data(self.conn, "download {}".format(remote_file_path))
                mode = 'wb'

        reply = req.recv_data(self.conn).decode('utf-8')
        reply_dict = json.loads(reply)
        if not reply_dict['status']:
            print(reply_dict['error'])
        else:
            print("开始下载")  # print(reply_dict['data'])
            req.recv_save_file_with_progress(self.conn, local_file_path, mode, seek=seek)
            print("下载完毕")


handler = Handler()
