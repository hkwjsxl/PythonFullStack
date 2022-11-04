import os
import struct


def send_data(conn, content, *args, **kwargs):
    data = content.encode('utf-8')
    header = struct.pack('i', len(data))
    conn.sendall(header)
    conn.sendall(data)


def recv_data(conn, chunk_size=1024):
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
    return has_read_data.decode('utf-8')


def recv_file(conn, save_file_name, chunk_size=1024):
    save_file_path = os.path.join('files', save_file_name)

    has_read_size = 0
    bytes_list = []
    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size)
        bytes_list.append(chunk)
        has_read_size += len(chunk)
    header = b"".join(bytes_list)

    data_length = struct.unpack('i', header)[0]
    file_object = open(save_file_path, mode='wb')
    has_read_data_size = 0
    while has_read_data_size < data_length:
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)
        file_object.write(chunk)
        file_object.flush()
        has_read_data_size += len(chunk)
    file_object.close()


def client_recv_file(conn, save_file_name, current_seek=0, chunk_size=1024):
    has_read_size = 0
    bytes_list = []
    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size)
        bytes_list.append(chunk)
        has_read_size += len(chunk)
    header = b"".join(bytes_list)

    data_length = struct.unpack('i', header)[0]
    if current_seek:
        mode = 'ab'
    else:
        mode = 'wb'
    file_object = open(save_file_name, mode=mode)
    has_read_data_size = current_seek
    while has_read_data_size < data_length:
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)
        file_object.write(chunk)
        file_object.flush()
        has_read_data_size += len(chunk)
    file_object.close()


def send_file(conn, file_path, current_seek=0):
    file_size = os.stat(file_path).st_size
    header = struct.pack('i', file_size)
    conn.sendall(header)

    has_send_size = 0
    file_object = open(file_path, mode='rb')
    if current_seek:
        file_object.seek(current_seek)
    while has_send_size < file_size:
        chunk = file_object.read(2048)
        conn.sendall(chunk)
        has_send_size += len(chunk)
    file_object.close()
