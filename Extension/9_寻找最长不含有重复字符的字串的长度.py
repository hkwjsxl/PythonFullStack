"""
	abcabcbb --> abc
	bbbbbb --> b
	pwwkew --> wke
"""


def length_no_repeat_of_max(s):
    map_dict = {}
    start = 0
    max_length = 0
    for index, value in enumerate(s):
        element_index = map_dict.get(value, 0)
        if element_index >= start:
            # start位置重置为当前元素的下一个位置的索引
            start = element_index + 1
        # 如果当前索引位置减去不重复元素的起始位置+1大于最大长度，就更新最大长度
        if index - start + 1 > max_length:
            max_length = index - start + 1
        # 将字符串当前元素的值和索引放入字典中
        map_dict[value] = index
    return max_length


if __name__ == '__main__':
    print(length_no_repeat_of_max("abcabcbb"))
    print(length_no_repeat_of_max("bbbbbb"))
    print(length_no_repeat_of_max("pwwkew"))
