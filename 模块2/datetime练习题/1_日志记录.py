"""日志记录，将用户输入的信息写入到文件，文件名格式为`年-月-日-时-分.txt`"""
from datetime import datetime


def main():
    while True:
        content = input('请输入要记录的信息：').strip()
        if content.upper() == 'Q':
            break
        current_datetime = datetime.now().strftime('%Y-%m-%d-%H-%M')
        with open('{}.txt'.format(current_datetime), 'a', encoding='utf-8') as f:
            f.write(content)
            f.flush()


if __name__ == '__main__':
    main()
