def extend_list(val, data=[]):
    data.append(val)
    return data


list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list("a")

print(list1, list2, list3)


"""
[10, 'a']
[123]
[10, 'a']
"""

