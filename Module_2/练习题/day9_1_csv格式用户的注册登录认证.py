import os


def main():
    while True:
        is_register = input('Y/N>>>').strip()
        is_register = is_register.upper()
        if is_register not in ('Y', 'N'):
            print('输入格式不正确！')
            continue
        if is_register == 'N':
            break
        user = input('user:>>>').strip()
        pwd = input('pwd:>>>').strip()
        with open(file_path, 'r+', encoding='utf-8') as f:
            for line in f:
                username = line.split(':')[0]
                if user != username:
                    continue
                print(f'{user}已存在！')
                break
            else:
                f.write(f'{user}:{pwd}\n')
                print(f'{user}注册成功！')
    # login
    print('login'.center(50, '-'))
    while True:
        username = input('username:>>>').strip()
        password = input('password:>>>').strip()
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                user, pwd = line.strip().split(':')
                if user == username and pwd == password:
                    print('登录成功！')
                    break
            else:
                print('登录失败！')
                continue
            break


if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_path, 'files')
    file_path = os.path.join(dir_path, 'user.csv')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    main()
