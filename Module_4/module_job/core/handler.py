from datetime import datetime
from functools import wraps

from utils import db_common
from utils.common import TextMethod, UserDict
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
        while True:
            title = validate_input('请输入文章标题:>>>')
            if title.upper() == 'Q':
                break
            content = validate_input('请输入文章内容:>>>')
            article_time = datetime.now()
            result = db_common.publish_article(
                self.LOGIN_USER_DICT.username,
                title=title,
                content=content,
                article_time=article_time
            )
            if result:
                print(f'{title}***发布成功!'.center(50, '-'))
                break
            print('发布失败!'.center(50, '*'))

    def look_article_list(self):
        article_list = db_common.look_article_list()
        if not article_list:
            print('暂时没有文章!'.center(50, '*'))
            return

        article_count = len(article_list)
        page_article_num = 2
        page_total_num = article_count / page_article_num
        v1, v2 = divmod(page_total_num, 2)
        if v2 not in (0, 1):
            page_total_num = int(page_total_num) + 1

        while True:
            print(f'共有{article_count}篇文章，{page_total_num}页'.center(50, '-'))
            page_num = input('请输入要查看的页数(每页2篇):>>>').strip()
            if page_num.upper() == 'Q':
                break
            if not page_num or not page_num.isdecimal():
                print('页码输入不正确!')
                continue
            page_num = int(page_num)
            if page_num < 1 or page_num > page_total_num:
                print('页码超出!')
                continue

            start_num = page_article_num * page_num - 1
            end_num = page_article_num * page_num
            part_article_list = article_list[start_num - 1:end_num]
            for article_dict in part_article_list:
                print(article_dict)

            while True:
                self.NAVIGATION.append('文章详情')
                print(' > '.join(self.NAVIGATION).center(50, '-'))

                choice = input('请输入看查看文章的ID(全文):>>>').strip()
                if choice.upper() == 'Q':
                    break
                if not choice or not choice.isdecimal():
                    print('序号输入不合法!')
                    continue
                choice = int(choice)
                if choice < 1 or choice > article_count:
                    print('页码超出!')
                    self.NAVIGATION.pop(-1)
                    continue
                choice -= 1
                try:
                    article = article_list[choice]
                except IndexError as e:
                    print('序号超出!')
                    self.NAVIGATION.pop(-1)
                    continue

                self.wrapper_login(self.article_detail(article))
                self.NAVIGATION.pop(-1)
                break

    def article_detail(self, article):
        article_id = article.get('id')
        # 阅读数量+1
        db_common.add_read_num(article_id)
        # 展示文章详情
        article_deatil = db_common.show_article_detail(article_id)
        print(article_deatil)

        user_id = self.LOGIN_USER_DICT.id

        def publish_comment():
            content = validate_input('请输入评论内容:>>>')
            comment_time = datetime.now()
            result = db_common.publish_comment(user_id, article_id, content, comment_time)
            if result:
                print('评论成功')
                return
            print('评论失败')

        def add_up_num():
            result = db_common.add_up_num(user_id, article_id)
            if result:
                print('点赞成功!')
                return
            print('点赞失败!')

        def add_down_num():
            result = db_common.add_down_num(user_id, article_id)
            if result:
                print('点踩成功!')
                return
            print('点踩失败!')

        func_dict = {
            '1': TextMethod('发表评论', self.wrapper(publish_comment)),
            '2': TextMethod('点赞', self.wrapper(add_up_num)),
            '3': TextMethod('点踩', self.wrapper_login(add_down_num)),
        }
        while True:
            print(' > '.join(self.NAVIGATION).center(50, '-'))
            for num, cls in func_dict.items():
                print(num, cls.text)

            choice = input('请输入序号:>>>').strip()
            if choice.upper() == 'Q':
                break
            if not choice or not choice.isdecimal():
                print('非法输入!')
                continue
            if choice not in func_dict.keys():
                print('输入不正确!')
                continue
            content = func_dict.get(choice)
            self.NAVIGATION.append(content.text)
            content.method()
            self.NAVIGATION.pop(-1)

    def logout(self):
        self.LOGIN_USER_DICT.clear()
        print('注销成功!')
        return 'logout'

    def run(self):
        self.NAVIGATION.append('首页')
        mapping_dict = {
            '1': TextMethod('注册', self.wrapper(self.register)),
            '2': TextMethod('登录', self.wrapper(self.login)),
            '3': TextMethod('发布文章', self.wrapper_login(self.publish_article)),
            '4': TextMethod('查看文章列表', self.wrapper_login(self.look_article_list)),
            '5': TextMethod('注销', self.wrapper_login(self.logout)),
        }
        while True:
            print(' > '.join(self.NAVIGATION).center(50, '-'))
            for num, cls in mapping_dict.items():
                print(num, cls.text)

            choice = input('请输入序号:>>>').strip()
            if choice.upper() == 'Q':
                break
            if not choice or not choice.isdecimal():
                print('非法输入!')
                continue
            if choice not in mapping_dict.keys():
                print('输入不正确!')
                continue
            content = mapping_dict.get(choice)
            self.NAVIGATION.append(content.text)
            content.method()
            self.NAVIGATION.pop(-1)


handler = Handler()
