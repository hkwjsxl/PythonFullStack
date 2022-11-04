import os
import requests
import shutil


def down_file():
    file_url = 'https://files.cnblogs.com/files/wupeiqi/HtmlStore.zip'
    res = requests.get(url=file_url)
    with open(file_path, 'wb') as f:
        print(res.content)
        f.write(res.content)


def main():
    # 1.下载文件
    # down_file()
    # 2.将下载的文件保存到当前执行脚本同级目录下 /files/package/ 目录下（且文件名为HtmlStore.zip）
    # 3.在将下载下来的文件解压到 /files/html/ 目录下
    file_new_path = os.path.join(dir_path, 'html')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    shutil.unpack_archive(file_path, file_new_path, format='zip')


if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_path, 'files')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, 'HtmlStore.zip')

    main()
