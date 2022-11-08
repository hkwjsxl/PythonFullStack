# -*- coding: utf-8 -*-

def get_text():
    txt = open("1.txt", "r", encoding='UTF-8').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
    return txt


file_txt = get_text()
words = file_txt.split()  # 对字符串进行分割，获得单词列表
counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(5):
    word, count = items[i]
    print("{0:<5}->{1:>5}".format(word, count))
