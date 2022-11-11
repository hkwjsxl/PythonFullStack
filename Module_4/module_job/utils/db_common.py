from datetime import datetime

from utils.db import Connect
from utils.common import enc_passwrod


def register(*args, **kwargs):
    kwargs['password'] = enc_passwrod(kwargs['password'])
    with Connect() as conn:
        sql = 'insert into userinfo(username,nickname,password,phone,email,create_time) ' \
              'values(%(username)s,%(nickname)s,%(password)s,%(phone)s,%(email)s,%(create_time)s);'
        return conn.exec(sql, **kwargs)


def login(*args, **kwargs):
    kwargs['password'] = enc_passwrod(kwargs['password'])
    with Connect() as conn:
        sql = 'select id, username, password from userinfo ' \
              'where username=%(username)s and password=%(password)s;'
        return conn.fetch_one(sql, **kwargs)


def user_exists(username):
    with Connect() as conn:
        sql = 'select id, username from userinfo where username=%s;'
        return conn.exec(sql, username)


def get_user_info(username):
    with Connect() as conn:
        sql = 'select * from userinfo where username=%s;'
        return conn.fetch_one(sql, username)


def publish_article(username, *args, **kwargs):
    with Connect() as conn:
        sql = 'select id from userinfo where username=%s;'
        user_id = conn.fetch_one(sql, username).get('id')
        sql = 'insert into article (title,content,article_time,user_id) ' \
              'values(%(title)s,%(content)s,%(article_time)s,%(user_id)s);'
        return conn.exec(sql, **kwargs, user_id=user_id)


def look_article_list():
    with Connect() as conn:
        sql = 'select id,title,article_time,read_num,comment_num,up_num,down_num from article;'
        return conn.fetch_all(sql)


def add_read_num(article_id):
    with Connect() as conn:
        sql = 'update article set read_num=read_num+1 where id=%s'
        return conn.exec(sql, article_id)


def show_article_detail(article_id):
    with Connect() as conn:
        sql = 'select * from article where id=%s;'
        detail_dict = conn.fetch_one(sql, article_id)
        sql = 'select content from comment where article_id=%s;'
        comment_list = conn.fetch_all(sql, article_id)
        detail_dict['comment_list'] = comment_list
        return detail_dict


def publish_comment(user_id, article_id, content, comment_time):
    with Connect() as conn:
        sql = 'update article set comment_num=comment_num+1 where id=%s;'
        conn.exec(sql, article_id)
        sql = 'insert into comment (content,comment_time,user_id,article_id) ' \
              'values (%s,%s,%s,%s);'
        return conn.exec(sql, content, comment_time, user_id, article_id)


def add_up_num(user_id, article_id):
    with Connect() as conn:
        # 查询是否已经点赞
        sql = 'select id from up_and_down where user_id=%s and article_id=%s and up_num=1;'
        is_up = conn.fetch_one(sql, user_id, article_id)
        if is_up:
            print('请勿重复点赞!')
            return

        sql = 'insert into up_and_down (user_id,article_id,up_num,ctime) ' \
              'values (%s,%s,%s,%s);'
        return conn.exec(sql, user_id, article_id, 1, datetime.now())


def add_down_num(user_id, article_id):
    with Connect() as conn:
        sql = 'select id from up_and_down where user_id=%s and article_id=%s and down_num=1;'
        is_up = conn.fetch_one(sql, user_id, article_id)
        if is_up:
            print('请勿重复点踩!')
            return

        sql = 'insert into up_and_down (user_id,article_id,down_num,ctime) ' \
              'values (%s,%s,%s,%s);'
        return conn.exec(sql, user_id, article_id, 1, datetime.now())
