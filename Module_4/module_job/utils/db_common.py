from utils.conn_db import Connect
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


