### MySQL基本操作

##### 基本操作

~~~Python
# 管理员身份进入cmd
	cd 到Mysql目录下（添加到path后，后续无需cd）
	mysql -uroot -p  # 首次进入密码为空，回车进入

# 查看库名
	show databases;  # Mysql语句；为结束标志

# 退出
	quit; # 这两条语句都可以，并且可以不用加分号
	exit;

# 自动开启服务（将Mysql服务端制作成系统服务，开机自启动）
	mysqld --install
# 关闭
	mysqld --remove

# 查看进程
	tasklist
	tasklist |findstr PID号
# 杀死进程
	taskkill -f -pid PID号

# 修改密码(直接在终端改)
	mysqladmin -uroot -p原密码 password 新密码
# 方式1
	mysqladmin -uroot -p123 password '1'
# 方式2
	update mysql.user set password=password('123') where user='root' and host='localhost';
# 方式3
	set password=password('1');   修改当前用户的密码
# 方式4
	grant all on *.* to 'root'@'localhost' identified by '123';
    
# 忘记密码以无密码方式登录
	1.关闭Mysql服务端
	命令行的方式启动（让mysql跳过用户名密码验证功能）
		mysqld --skip-grant-tbles
	2.mysql -uroot -p 直接回车
	3.修改密码
		update mysql.user set password=password(密码) where user='root' and host='localhost';
	4.立刻将修改数据刷到硬盘
		flush privileges;
	5.关闭当前服务器，重新启动服务

# 将管理员用户名和密码添加到配置文件中
[mysql]
user="root"
password=密码

# 查看当前库名
	select database();
# 切换库
	use 库名;

# 取消操作
	\c
# 基本信息
	\s

~~~

##### 库的增删改查

~~~python
# 增
	create database db1;
	指定编码（默认utf8）
	create database db2 charset='gbk';
# 查
	show databases;  # 查所有
	show create database db1;  # 查单个
# 改
	alter database db1 charset='gbk';
# 删
	drop database db1;
	
~~~

##### 表的增删改查

~~~python
# 增
	create table t1(id char(6),name char(8));
# 查
	show tables;  # 当前库所有表名
	show create table t1;  # 查单个表
    describe t1;  # desc t1(简写)
# 改
	alter table t1 modify name char(8);
# 删
	drop table t1;
    
"""
create table db2.t1(id char);  绝对路径形式操作不同的库
"""

~~~

##### 数据的增删改查

~~~python
# 增
	insert into t1 values(1,'jon');  # 一条
    insert into t1 values(1,'jon'),(2,'liu'),(3,'li');  # 多条
# 查
	select * from t1;  # 数据较多时不建议使用
    select name from t1;  # 只显示name列
# 改
	update t1 set name='xing' where id > 3;
# 删
	delete from t1 where id > 3;
	delete from t1;  # 清空所有数据
    
~~~

### 存储引擎

##### MySQL主要存储引擎

-   innodb

    ​		MySQL5.5版本及之后默认的存储引擎

    ​		数据更加安全

-   myisam

    ​		MySQL5.5版本之前默认的存储引擎

    ​		查询速度快

-   memory

    ​		内存引擎（数据全部放在内存中），断电数据丢失

    ​		临时存储数据

-   blackhole

    ​		无论存什么，都立即消失（黑洞）

##### 查看所有存储引擎

~~~python
show engines;
~~~

##### 使用存储引擎

~~~python
create table t1(id int) engine='innodb';
create table t2(id int) engine='myisam';
create table t3(id int) engine='memory';
create table t4(id int) engine='blackhole';
~~~

### 严格模式

~~~python
# 查看严格模式
show variables like '%mode';

模糊匹配/查询
	关键字 like
    	%：匹配任意多个字符
        _：匹配任意单个字符
        
# 修改严格模式（默认为STRICT_TRANS_TABLES的不用修改）
	set session  # 只在当前窗口有效
    set global   # 全局有效
    
    set global sql_mode='STRICT_TRANS_TABLES';
    修改完后，要重新进入
~~~

### 基本类型

整型和单精度

| TINYINT      | 1 Bytes                                  | (-128，127)                                                  | (0，255)                                                     | 小整数值        |
| ------------ | ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------- |
| SMALLINT     | 2 Bytes                                  | (-32 768，32 767)                                            | (0，65 535)                                                  | 大整数值        |
| MEDIUMINT    | 3 Bytes                                  | (-8 388 608，8 388 607)                                      | (0，16 777 215)                                              | 大整数值        |
| INT或INTEGER | 4 Bytes                                  | (-2 147 483 648，2 147 483 647)                              | (0，4 294 967 295)                                           | 大整数值        |
| BIGINT       | 8 Bytes                                  | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807)      | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| FLOAT        | 4 Bytes                                  | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE       | 8 Bytes                                  | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL      | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | 小数值          |

##### 统计字段长度

~~~python
#char_length方法

select char_length(字段名) from 表名;
~~~

##### char&varchar

~~~python
char
	固定类型
	浪费空间
   	存取方便
    超出报错，不超默认用空格补全
    
varchar
	可变类型
    节省空间
    存取麻烦
    	1bytes+内容
    超出报错，不超默认有几个存几个
~~~

##### 枚举与集合类型

~~~python
enum  # 只能选一个
set  # 可以选多个

create table t1(
    id int,name char(8),gender enum('male','female','others'),hobby set('read','write')
);
insert into t1 values(
	1,'jon','male','read,write'
);

# 不能插入没有的值
~~~

##### 时间类型

~~~python
date  # 年月日
datetime  # 年月日时分秒
time  # 时分秒
year  # 年
...
~~~

### 约束条件

##### 宽度和约束条件的关系

宽度是用来限制数据的存储

约束条件是在宽度的基础之上增加的额外的约束

~~~python
"""
1、primary key(PK) ：主键约束
提升查询速度
设置为主键的列，此列的值必须非空且唯一，主键在一个表中只能有一个，但是可以有多个列一起构成。

2、not null ：非空约束
列值不能为空，也是表设计的规范，尽可能将所有的列设置为非空。可以设置默认值为0

3、unique key ：唯一约束
列值不能重复

4、unsigned ：无符号
针对数字列，非负数。

5、zerofill ：补0

"""
~~~

##### 约束非空

~~~python
create table t1(id int not null);

# 特例，int后面不用加()
# 针对整型字段 括号内无需指定宽度因为它默认的宽度以及足够显示所有的数据了
~~~

##### 唯一

~~~python
create table t1(id int unique);
~~~

##### 联合唯一

~~~python
create table t1(
	id int,
    ip char(20),
    port char(6),
    unique(ip,port)
);
~~~

##### 默认值

~~~python
create table t1(id int unique,name char(10),genter enum('male','female') default 'male')
~~~

##### 自增auto_increment

~~~python
create table t1(
    id int primary key auto_increment,
    name char(16) not null,
    genter enum('male','female') default 'male'
);

delete from t1;  # 删除表中数据后，主键的自增不会停止
truncate t1;  # 清空表数据并且重置主键

~~~

### show语句

~~~python
show databases;                         	#查看所有数据库
show tables;                                #查看当前库的所有表
SHOW tables from                  			#查看某个指定库下的表
show create database world                  #查看建库语句
show create table world.city                #查看建表语句
show grants for  root@'localhost'       	#查看用户的权限信息
show charset；                              #查看字符集
show collation                              #查看校对规则
show processlist;                           #查看数据库连接情况
show full processlist;						#查看数据库连接情况,且显示info的详细信息
show privileges								#查看支持的权限信息
show index from                             #表的索引情况
show status                                 #数据库状态查看
SHOW STATUS LIKE '%lock%';         			#模糊查询数据库某些状态
SHOW variables                             	#查看所有配置信息
SHOW variables LIKE '%lock%';          		#模糊查看部分配置信息
show engines                                #查看支持的所有的存储引擎
show engine innodb status\G                 #查看InnoDB引擎相关的状态信息
show binary logs                            #列举所有的二进制日志
show master status                          #查看数据库的日志位置信息
show binlog evnets                          #查看二进制日志事件
show master status;							#查询二进制日志的位置点信息
show slave status\G                         #查看从库状态
SHOW RELAYLOG EVENTS in       		  		#查看从库relaylog事件信息，查看中继日志事件
desc  (show colums from city)               #查看表的列定义信息
~~~























