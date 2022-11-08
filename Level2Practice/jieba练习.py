import jieba

if __name__ == '__main__':
    s = '好好学习，天天向上。'
    word_lst = jieba.lcut(s)  # 精简模式
    print(word_lst)
    word_lst = jieba.lcut(s, cut_all=True)  # 全模式
    print(word_lst)
    word_lst = jieba.lcut_for_search(s)  # 搜索引擎模式
    print(word_lst)





