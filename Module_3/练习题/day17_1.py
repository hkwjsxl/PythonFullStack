"""
# 需求
1. while循环提示用户输入: 户名、密码、邮箱(正则满足邮箱格式)
2. 为每个用户创建一个个对象，并添加到user_list中。
3. 当列表中的添加 3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱
"""
import re


class Obj:
    def __init__(self, name, pwd, email):
        self.name = name
        self.pwd = pwd
        self.email = email


user_list = []
while True:
    user = input("请输入用户名:")
    pwd = input("请输入密码:")
    email = input("请输入邮箱:")

    if not re.findall('\w+@\w+\.\w+', email):
        print('邮箱不合法！')
        continue

    user_list.append(Obj(user, pwd, email))
    if len(user_list) == 3: break

for user_obj in user_list:
    print(user_obj.name, user_obj.email)


