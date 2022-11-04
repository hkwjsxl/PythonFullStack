import os
import hashlib
from openpyxl import load_workbook


def calculation_a_num(char):
    if not isinstance(char, str):
        print(f'{char}不是字符串')
        return
    i = 0
    for v in char:
        if v.lower() == 'a':
            i += 1
    return i


def judge_len(args):
    if isinstance(args, int):
        args = str(args)
    if len(args) > 5:
        return True
    return False


def compare_is_big(n1, n2):
    if n1 > n2:
        return n1
    return n2


def join_args(*args):
    for i in args:
        if not isinstance(i, str):
            print(f'{i}不是字符串')
            return
    result = '*'.join(args)
    with open(r'files/student_msg.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def select_content(file_path, key):
    if not os.path.exists(file_path):
        return
    lst = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if key in line:
                lst.append(line)
        return tuple(lst)


def change_string(origin):
    # 补充代码，将字符串origin中中的敏感词替换为 **，最后将替换好的值返回。
    data_list = ["苍老师", "波多老师", "大桥"]
    for data in data_list:
        if data in origin:
            origin = origin.replace(data, '**')
    return origin


def encrypt(origin):
    origin_bytes = origin.encode('utf-8')
    md5_object = hashlib.md5()
    md5_object.update(origin_bytes)
    return md5_object.hexdigest()

def judge_user_pwd():
    sheet = load_workbook(r'files/user.xlsx')['Sheet1']
    user_dict = {}
    i = 0
    for row in sheet.rows:
        if i == 0:
            i += 1
            continue
        user_dict[row[1].value] = row[2].value

    print(user_dict)
    user = input('user:>>>').strip()
    pwd = input('pwd:>>>').strip()
    pwd = encrypt(pwd)
    for k, v in user_dict.items():
        if user == k and pwd == v:
            print('登录成功')
            return
    print('登录失败')

def main():
    # 1
    num = calculation_a_num('abcAbcAabbCC')
    print(num)
    # 2
    length = judge_len(123456789)
    # length = judge_len((123,1,2,3,123,6))
    # length = judge_len([123,1,2,3,123,6])
    print(length)
    # 3
    num = compare_is_big(1, 2)
    print(num)
    # 4
    join_args('hkw', '男', '18', '本科')
    # 5
    result = select_content("files/user.csv", "0224")
    if result is None:
        print('文件不存在')
    for line in result:
        print(line)
    # 6
    # text = input("请输入内容：").strip()
    # result = change_string(text)
    # print(result)
    # 7
    judge_user_pwd()



if __name__ == '__main__':
    main()
