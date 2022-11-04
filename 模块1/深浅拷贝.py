from copy import copy, deepcopy

l1 = [1, 2, 3, [1, 2]]
# l2 = copy(l1)
l2 = l1
# l2 = deepcopy(l1)
l3 = deepcopy(l1)
l1[3][0] = 3
print(l1)
print(l2)
print(l3)
"""

浅拷贝  值跟着改变
深拷贝  值不会跟着改变



"""