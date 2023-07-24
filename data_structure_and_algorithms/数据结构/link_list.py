"""链表"""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def create_link_head(li):
    # 从后往前链接：1<--2<--3<--4...
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def create_link_tail(li):
    # 从前往后链接：1-->2-->3-->4...
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_lk(lk):
    while lk:
        print(lk.data, end=',')
        lk = lk.next

# lk = Node(1)
# lk1 = Node(2)
# lk2 = Node(3)
# lk.next = lk1
# lk1.next = lk2
# print(lk.data)
# print(lk.next.data)
# print(lk.next.next.data)

# lk = create_link_head([1, 3, 4, 5, 6])
# print_lk(lk)
# print("\n---")
# lk = create_link_tail([1, 3, 4, 5, 6])
# print_lk(lk)
