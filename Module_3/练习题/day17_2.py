class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        print('login'.center(50, '-'))
        while True:
            user = input("请输入用户名:")
            pwd = input("请输入密码:")
            for user_obj in self.user_list:
                if user_obj.name == user and user_obj.pwd == pwd:
                    print('登录成功！')
                    break
            else:
                print('登录失败！')
                continue
            break

    def register(self):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        print('register'.center(50, '-'))
        user = input("请输入用户名:")
        pwd = input("请输入密码:")
        self.user_list.append(User(user, pwd))

    def run(self):
        """
        主程序
        :return:
        """
        print('run'.center(50, '-'))
        while True:
            self.register()
            con = input('是否继续Y/N:>>>').strip()
            if con.upper() == 'N':
                break
        self.login()


if __name__ == '__main__':
    obj = Account()
    obj.run()
