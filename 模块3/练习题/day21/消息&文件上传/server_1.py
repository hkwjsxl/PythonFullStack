import socket
import struct
import json


def get_msg(conn, chunk_size=1024):
    read_size = 0
    read_data = b''
    while read_size < 4:
        chunk = conn.recv(4 - read_size)
        read_data += chunk
        read_size += len(chunk)
    data_length = struct.unpack('i', read_data)[0]

    read_size = 0
    has_read_data = b''
    while read_size < data_length:
        size = chunk_size if chunk_size < (data_length - read_size) else data_length - read_size
        has_read_data += conn.recv(size)
        read_size += size
    return has_read_data


def get_file(conn, file_name, chunk_size=1024):
    read_size = 0
    read_data = b''
    while read_size < 4:
        chunk = conn.recv(4 - read_size)
        read_data += chunk
        read_size += len(chunk)
    data_length = struct.unpack('i', read_data)[0]

    with open(file_name, 'wb') as f:
        read_size = 0
        while read_size < data_length:
            size = chunk_size if (data_length - read_size) > chunk_size else data_length - read_size
            f.write(conn.recv(size))
            f.flush()
            read_size += size


def run():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8001))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        while True:
            data = get_msg(conn).decode('utf-8')
            if data == 'close':
                print('quit')
                break
            json_data = json.loads(data)
            if json_data['msg_type'] == 'msg':
                return_data = get_msg(conn)
                print(return_data.decode('utf-8'))
            else:
                get_file(conn, json_data['file_name'])
                print('文件路径%s' % json_data['file_name'])
        conn.close()
    server.close()


if __name__ == '__main__':
    run()
