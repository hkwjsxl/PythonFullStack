from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BinaryTreeNode("A")
b = BinaryTreeNode("B")
c = BinaryTreeNode("C")
d = BinaryTreeNode("D")
e = BinaryTreeNode("E")
f = BinaryTreeNode("F")
g = BinaryTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e  # 树的根

"""
          E
    A         G
       C          F
    B     D
"""


def perv_order(root):
    """前序遍历"""
    if root:
        print(root.data, end=",")
        perv_order(root.lchild)
        perv_order(root.rchild)


def in_order(root):
    """中序遍历"""
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)


def post_order(root):
    """后序遍历"""
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


def level_order(root):
    """层次遍历：借助队列"""
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        now_node = queue.popleft()
        print(now_node.data, end=",")
        if now_node.lchild:
            queue.append(now_node.lchild)
        if now_node.rchild:
            queue.append(now_node.rchild)


perv_order(root)
print()
in_order(root)
print()
post_order(root)
print()
level_order(root)
print()
