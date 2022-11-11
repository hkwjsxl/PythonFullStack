~~~python
"""
基于现在掌握的知识点，设计一下博客系统的部分功能。
根据业务需求设计相关的表结构，内部需涵盖如下功能：
1 登录、注册
2 发布博客
3 查看博客列表
    显示博客标题、创建时间、阅读数量、评论数量、赞数量 等。（支持分页查看）
4 博客详细，显示博文详细、评论等（*）。
    发表评论
    赞 or 踩
    阅读数量 + 1
"""
~~~

~~~python
"""
userinfo
    username,password,nickname,phone,email,
article
    title,content,article_time,read_num,comment_num,up_num,down_num,user_id
comment
    user_id,article_id,content,comment_time
up_and_down
    user_id
    article_id
    up_num
    down_num
    
"""
~~~

~~~sql
create table userinfo(
    id int not null primary key auto_increment,
    username varchar(32) not null,
    nickname varchar(32) not null,
    password varchar(32) not null,
    phone varchar(11) not null,
    email varchar(32) not null,
    create_time datetime default Now() not null,
    unique ix_username (username),
    unique ix_phone (phone),
    unique ix_email (email),
    index ix_user_pwd (username,password),
    index ix_nick_pwd (nickname,password)
);

create table article(
    id int not null primary key auto_increment,
    title varchar(64) not null,
    content varchar(255) not null,
    article_time datetime default Now() not null,
    read_num int default 0,
    comment_num int default 0,
    up_num int default 0,
    down_num int default 0,
    
    user_id int not null,
    constraint fk_article_userinfo foreign key (user_id) references userinfo(id)
);

create table comment(
    id int not null primary key auto_increment,
    content varchar(255) null,
    comment_time datetime default Now() not null,
    
    user_id int not null,
    article_id int not null,
    constraint fk_comment_userinfo foreign key (user_id) references userinfo(id),
    constraint fk_comment_article foreign key (article_id) references article(id)
);

create table up_and_down(
    id int not null primary key auto_increment,
    up_num int default 0,
    down_num int default 0,
    ctime datetime default Now() not null,
    
    user_id int not null,
    article_id int not null,
    constraint fk_updown_userinfo foreign key (user_id) references userinfo(id),
    constraint fk_updown_article foreign key (article_id) references article(id)
);
~~~

~~~python
# userinfo
hkw,0224
jon,123
~~~

