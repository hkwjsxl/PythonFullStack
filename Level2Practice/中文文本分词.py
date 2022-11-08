# -*- coding: utf-8 -*-
import jieba

txt = open("三国演义.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)  # 使用精确模式对文本进行分词
counts = {}  # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:  # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序

for i in range(3):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
