"""编写一个函数，这个函数接受一个文件夹名称作为参数，寻找文件夹中所有文件的路径并输入（包含嵌套）。"""
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def run(dir_path):
    for base_path, dir_name, file_name_list in os.walk(dir_path):
        # print(base_path, dir_name, file_name_list)
        for file_name in file_name_list:
            file_path = os.path.join(base_path, file_name)
            print(file_path)


if __name__ == '__main__':
    run(BASE_PATH)
