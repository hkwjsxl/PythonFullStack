"""
有一个数据结构如下所示，请编写一个函数从该结构数据中返画由指定的 字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。
fields:由"|"连接的以fld开头的字符串, 如fld2|fld7|fld29

def select(fields):
    print(DATA)
    return result
"""


def run():
    DATA = {
        "time": "2016-08-05T13:13:05",
        "some_id": "ID1234",
        "grp1": {"fld1": 1, "fld2": 2, },
        "xxx2": {"fld3": 0, "fld4": 0.4, },
        "fld6": 11,
        "fld7": 7,
        "fld46": 8
    }
    new_dict = {}
    filed = input('请输入要分割的字段(|)：').strip()
    filed_list = filed.split('|')
    for value in filed_list:
        value = value.strip()
        if value in DATA.keys():
            new_dict[value] = DATA.get(value)
    print(new_dict)


if __name__ == '__main__':
    run()
