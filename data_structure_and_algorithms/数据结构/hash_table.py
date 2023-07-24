"""
使用链表，实现hash。构建一个类似于集合的hash表
"""


class LinkList:
    """对链表的进一步封装"""

    class Node:
        """链表的节点类"""

        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        """将链表转为迭代器类"""

        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                current_node = self.node
                self.node = current_node.next
                return current_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        """使用尾插法，进行插入"""
        current_node = LinkList.Node(obj)
        if not self.head:
            self.head = current_node
            self.tail = current_node
        else:
            self.tail.next = current_node
            self.tail = current_node

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<" + ", ".join(map(str, self)) + ">>"


class HashTable:
    """实现集合的部分功能，不可重复，可查询（拉链法）"""

    def __init__(self, size=100):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]

    def h(self, k):
        return k % self.size

    def find(self, k):
        hash_num = self.h(k)  # 获取给定数值的hash值
        return self.T[hash_num].find(k)

    def insert(self, k):
        if self.find(k):
            # 不可重复
            print("Duplicated Insert.")
        else:
            hash_num = self.h(k)  # 获取插入的值的hash值
            self.T[hash_num].append(k)


ht = HashTable()

ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(103)
ht.insert(200)

print(",".join(map(str, ht.T)))
print(ht.find(0))
print(ht.find(103))
print(ht.find(200))
