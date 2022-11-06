"""
create table news(
    id int not null auto_increment primary key,
    nid int not null,
    title varchar(128),
    url varchar(128)
);
"""

import pymysql
from pymysql.cursors import DictCursor


def run():
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root123',
        db='day25',
        charset='utf8',
    )
    cursor = db.cursor(DictCursor)
    try:

        with open('news.csv', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                nid, orther = line.split(',', maxsplit=1)
                title, url = orther.rsplit(',', maxsplit=1)
                sql = 'insert into news (nid, title, url) values (%s,%s,%s);'
                cursor.execute(sql, (nid, title, url))
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    run()
