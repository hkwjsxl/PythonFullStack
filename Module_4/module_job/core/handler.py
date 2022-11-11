from functools import wraps
from utils.common import TextMethod


class Handler:
    ...
    NAVIGATION = []

    def wrapper(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(' > '.join(self.NAVIGATION).center(50, '-'))
            func()

        return inner

    def register(self):
        ...

    def login(self):
        ...

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
            '3': TextMethod('发布文章', self.wrapper(self.publish_article)),
            '4': TextMethod('查看文章列表', self.wrapper(self.look_article_list)),
            '5': TextMethod('文章详情', self.wrapper(self.article_detail)),
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
