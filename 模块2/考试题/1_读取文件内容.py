"""一个大小为100G的文件 etl_log.txt，要读取文件中的内容，写出具体过程代码。"""
import os


def run(file_path):
    # with open(file_path, 'r', encoding='utf-8') as f:
    #     for line in f:
    #         line = line.strip()
    #         print(line)

    # 如果文件只有一行
    read_size = 0
    file_size = os.path.getsize(file_path)
    data_total = b''
    with open(file_path, 'rb') as f:
        while read_size < file_size:
            read_data = f.read(8)
            read_size += len(read_data)
            data_total += read_data
        print(file_size)
        print(read_size)
        print(data_total.decode('utf-8'))


if __name__ == '__main__':
    run(r'files/etl_log.txt')
