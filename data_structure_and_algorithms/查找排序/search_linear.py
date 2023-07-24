"""顺序查找"""


def linear_search(lst, val):
    for index, value in enumerate(lst):
        if value == val:
            return index
    return


ret = linear_search([9, 8, 6, 2, 1, 4], 2)
print(ret)
