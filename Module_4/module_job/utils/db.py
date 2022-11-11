import pymysql
from pymysql.cursors import DictCursor
from dbutils.pooled_db import PooledDB

from settings import DB_POOL_CONN

MYSQL_DB_POOL = PooledDB(
    creator=pymysql,
    **DB_POOL_CONN
)


class Connect:
    def __init__(self):
        self.conn = conn = MYSQL_DB_POOL.connection()
        self.cursor = conn.cursor(DictCursor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    def exec(self, sql, *args, **kwargs):
        params = args or kwargs
        # print(params)
        row = self.cursor.execute(sql, params)
        self.conn.commit()
        return row

    def fetch_one(self, sql, *args, **kwargs):
        params = args or kwargs
        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        return result

    def fetch_all(self, sql, *args, **kwargs):
        params = args or kwargs
        self.cursor.execute(sql, params)
        result = self.cursor.fetchall()
        return result
