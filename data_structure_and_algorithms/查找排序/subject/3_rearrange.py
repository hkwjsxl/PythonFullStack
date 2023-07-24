"""
给两个字符串s和t，判断t是否为s的重新排列后组成的单词
`s = "anagram", t = "nagaram", return true.`
`s = "rat", t = "car", return false.`
"""


# 方法一
def rearrange(s, t):
    """
    :param s: 第一个字符串
    :param t: 第二个字符串
    :return: True or False
    """
    tmp_dic = {}
    flag = True
    for val in s:
        tmp_dic[val] = tmp_dic.get(val, 0) + 1
    for val in t:
        ret = tmp_dic.get(val, -1)
        if ret == -1:
            flag = False
            break
        tmp_dic[val] -= 1
        if tmp_dic[val] == 0:
            tmp_dic.pop(val)
    if bool(tmp_dic):
        return False
    return flag


# 方法二（排序）
def rearrange(s, t):
    """
    :param s: 第一个字符串
    :param t: 第二个字符串
    :return: True or False
    将两个字符串排好序，如果排完序的字符串相等，就返回True
    """
    return sorted(list(s)) == sorted(list(t))


# 方法三
def rearrange(s, t):
    """
    :param s: 第一个字符串
    :param t: 第二个字符串
    :return: True or False
    用两个字典保存字符串中的字符数量，如果两个字符串的字符数量相同，就返回True
    """
    tmp_dic1 = {}
    tmp_dic2 = {}
    for val in s:
        tmp_dic1[val] = tmp_dic1.get(val, 0) + 1
    for val in t:
        tmp_dic2[val] = tmp_dic2.get(val, 0) + 1
    return tmp_dic1 == tmp_dic2


print(rearrange("anagram", "nagaram"))
print(rearrange("rat", "car"))
