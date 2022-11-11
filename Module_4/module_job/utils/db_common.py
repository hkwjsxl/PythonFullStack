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
        sql = 'select id, username, password from userinfo where username=%(username)s and password=%(password)s;'
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
