"""
count = 0
with open(r'file\access.log', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('223.73.89.192'):
            count += 1

print(count)

"""

"""

dic = {}
with open(r'file\access.log', 'r', encoding='utf-8') as f:
    for line in f:
        ip = line.split(' ')[0]
        if ip not in dic:
            dic[ip] = 0
        dic[ip] += 1

print(dic)

"""

"""
with open(r'file\gupiao.txt', 'r', encoding='utf-8') as f:
    f.readline()
    for line in f:
        line = line.strip()
        price = line.split(',')[2]
        price = float(price)
        if price > 20:
            print(line)

"""

"""

import shutil

with open(r'file\ha.conf', 'r', encoding='utf-8') as f1, \
        open(r'file\ha_new.conf', 'a', encoding='utf-8') as f2:
    for line in f1:
        line = line.replace('luffycity', 'pythonav')
        f2.write(line + '\n')
shutil.move(r'file\ha_new.conf', r'file\ha.conf')

"""

import re

file_name = r'abc\d/s:f*s?df"fs<d>sd|ef'
file_name = re.sub(r'[\\/:*?"<>|]', '', file_name)
print(file_name)
