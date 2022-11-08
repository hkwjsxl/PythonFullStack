# 创建表
"""
create table class (
    cid int not null primary key auto_increment,
    caption varchar(16) not null
);
create table teacher(
    tid int not null primary key auto_increment,
    tname varchar(16) not null
);
create table student(
    sid int not null primary key auto_increment,
    sname varchar(16) not null,
    gender varchar(8) not null,
    class_id int not null,
    constraint fk_student_class foreign key (class_id) references depart(cid)
);
create table course(
    cid int not null primary key auto_increment,
    cname varchar(16) not null,
    teacher_id int not null,
    constraint fk_course_teacher foreign key (teacher_id) references depart(tid)
);
create table score(
    sid int not null primary key auto_increment,
    student_id int not null,
    course_id int not null,
    num int not null,
    constraint fk_score_student foreign key (student_id) references depart(sid),
    constraint fk_score_cource foreign key (course_id) references depart(cid)
);

"""

# 添加数据
"""
insert into class(cid,caption) values(1, "三年二班"),(2, "一年三班"),(3, "三年一班");
insert into teacher(tid,tname) values(1, "波多"),(2, "苍空"),(3, "饭岛");
insert into student(sid,sname,gender,class_id) values(1, "钢蛋", "女", 1),(2, "铁锤", "女", 1),(3, "山炮", "男", 2);
insert into course(cid,cname,teacher_id) values(1, "生物", 1),(2, "体育", 1),(3, "物理", 2);
insert into score(sid,student_id,course_id,num) values(1, 1, 1, 60),(2, 1, 2, 59),(3, 2, 2, 100);


INSERT INTO student VALUES ('1','理解', '男', '1'), ('2', '钢蛋', '女', '1'), ('3', '张三', '男', '1'), ('4', '张一', '男', '1'), ('5', '张二', '女', '1'), ('6', '张四','男', '1'), ('7', '铁锤', '女', '2'), ('8', '李三', '男', '2'), ('9', '李一', '男', '2'), ('10', '李二', '女', '2'), ('11', '李四', '男', '2'), ('12', '如花', '女', '3'), ('13', '刘三', '男', '3'), ('14', '刘一', '男', '3'), ('15',  '刘二', '女','3'), ('16', '刘四', '男', '3');


"""
