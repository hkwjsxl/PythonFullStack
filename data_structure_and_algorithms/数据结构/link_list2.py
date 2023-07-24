"""双链表"""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


lk = Node(1)
lk1 = Node(2)
lk2 = Node(3)
lk.next = lk1
lk1.next = lk2
lk1.prev = lk
lk2.prev = lk1
print(lk.data)
print(lk.next.data)
print(lk.next.next.data)
print(lk.prev)
print(lk.next.prev.data)
print(lk.next.next.prev.prev.data)
