from datetime import datetime
from functools import wraps

from utils.common import TextMethod, UserDict
from utils import db_common
from utils.validator import validate_input, validate_email, validate_phone


class Handler:
    NAVIGATION = []
    LOGIN_USER_DICT = UserDict()

    def wrapper(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(' > '.join(self.NAVIGATION).center(50, '-'))
            func(*args, **kwargs)

        return inner

    def wrapper_login(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            if not self.LOGIN_USER_DICT.username:
                print('请先登录!'.center(50, '-'))
                return
            print(' > '.join(self.NAVIGATION).center(50, '-'))
            func(*args, **kwargs)

        return inner

    def register(self):
        while True:
            username = validate_input('请输入要注册的用户名:>>>')
            if username.upper() == 'Q':
                break
            result = db_common.user_exists(username)
            if result:
                print('用户名已存在!')
                continue
            nickname = validate_input('请输入要注册的用户别名:>>>')
            password = validate_input('请输入密码:>>>')
            phone = validate_input('请输入手机号:>>>', role=validate_phone)
            email = validate_input('请输入邮箱:>>>', role=validate_email)
            create_time = datetime.now()
            result = db_common.register(
                username=username,
                nickname=nickname,
                password=password,
                phone=phone,
                email=email,
                create_time=create_time
            )
            if result:
                print('注册成功'.center(50, '-'))
                break
            print('注册失败'.center(50, '-'))

    def login(self):
        while True:
            username = validate_input('请输入用户名:>>>')
            if username.upper() == 'Q':
                break
            password = validate_input('请输入密码:>>>')
            result = db_common.login(username=username, password=password)
            if result:
                print('登录成功!'.center(50, '-'))
                userinfo_dict = db_common.get_user_info(username)
                self.LOGIN_USER_DICT.set_info(userinfo_dict)
                break
            print('用户名或密码错误!'.center(50, '-'))

    def publish_article(self):

        ...

    def look_article_list(self):
        ...

    def article_detail(self):
        ...

    def run(self):
        self.NAVIGATION.append('首页')
        mapping_dict = {
            '1': TextMethod('注册', self.wrapper(self.register)),
            '2': TextMethod('登录', self.wrapper(self.login)),
            '3': TextMethod('发布文章', self.wrapper_login(self.publish_article)),
            '4': TextMethod('查看文章列表', self.wrapper_login(self.look_article_list)),
            '5': TextMethod('文章详情', self.wrapper_login(self.article_detail)),
        }

        while True:
            print(' > '.join(self.NAVIGATION).center(50, '-'))
            for num, cls in mapping_dict.items():
                print(num, cls.text)

            choice = input('请输入序号:>>>').strip()
            if choice.upper() == 'Q':
                print('退出!')
                break
            if not choice:
                print('请输入非空序号!')
                continue
            if not choice.isdecimal():
                print('请输入数字序号!')
                continue
            if choice not in mapping_dict.keys():
                print('输入不正确!')
                continue
            content = mapping_dict.get(choice)
            self.NAVIGATION.append(content.text)
            content.method()
            self.NAVIGATION.pop(-1)


handler = Handler()
