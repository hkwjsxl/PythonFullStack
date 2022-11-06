"""
create table admin(
    id int not null primary key auto_increment,
    name varchar(32) not null,
    password varchar(64) not null,
    gender char(1) not null,
    email varchar(64),
    amount decimal(10,2) not null default 0,
    ctime datetime
);

insert into admin(name,password,gender,email,amount,ctime) values("武沛齐","123123","男","xxx@live.com",19991.12,NOW());
insert into admin(name,password,gender,email,amount,ctime) values("alex","sb","男","alex@live.com",991.12,NOW());
insert into admin(name,password,gender,email,amount,ctime) values("eric","8888","女","eric@live.com",991.12,NOW());
insert into admin(name,password,gender,email,amount,ctime) values("tony","123123123","女","xxxxxxxx@live.com",200.12,NOW()), ("kelly","8888","女","kelly@live.com",991.12,NOW());

update admin set gender="男" where id>3;

select * from admin where amount>1000;

update admin set amount=amount + 1000;

delete from admin where gender="男";


"""
import datetime
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
        autocommit=True
    )
    cursor = db.cursor(DictCursor)

    # 添加单条
    # sql = 'insert into admin(name,password,gender,email,amount,ctime) values("hkw","123","男","hkw@live.com",180000,NOW());'
    # cursor.execute(sql)

    # 添加多条
    # sql = 'insert into admin(name,password,gender,email,amount,ctime) values(%s,%s,%s,%s,%s,%s);'
    # cursor.executemany(sql, [
    #     ["jon", "123", "男", "xxx@live.com", 666, datetime.datetime.now()],
    #     ["tom", "s123b", "男", "xxx@live.com", 777, datetime.datetime.now()],
    # ])

    # 将 `id>3`的所有人的性别改为  男。
    # sql = 'update admin set gender="男" where id>3;'
    # cursor.execute(sql)

    # 查询余额 `amount>1000`的所有用户。
    # sql = 'select * from admin where amount>1000;'

    # 让每个人的余额在自己原的基础上 +1000 。
    # sql = 'update admin set amount=amount+1000;'

    # 删除性别为男的所有数据。
    # sql = 'delete from admin where gender="男";'
    # cursor.execute(sql)

    cursor.close()
    db.close()


if __name__ == '__main__':
    run()
