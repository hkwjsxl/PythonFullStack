"""删除文件夹"""
import os
import shutil


# os.removedirs(r'dir_path')  # 文件夹非空时，报错(删除空文件夹，一层)
shutil.rmtree(r'dir_path')  # 直接删除(多层)

