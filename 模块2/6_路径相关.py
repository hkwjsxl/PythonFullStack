import os

base_path = os.path.abspath(__file__)
dir_path = os.path.dirname(base_path)
# 避免系统路径斜杠不匹配
file_path = os.path.join(dir_path, 'file', 'info.txt')

print(base_path)
print(dir_path)
print(file_path)
