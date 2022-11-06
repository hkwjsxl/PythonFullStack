import shutil

# 压缩文件
shutil.make_archive(root_dir='file', base_name='file_new', format='zip')
# 解压文件
shutil.unpack_archive('file_new.zip', r'file_new\x\xx', format='zip')
