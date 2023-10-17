"""
描述
请实现两个函数，分别用来序列化和反序列化二叉树，不对序列化之后的字符串进行约束，但要求能够根据序列化之后的字符串重新构造出一棵与原二叉树相同的树。

二叉树的序列化(Serialize)是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树等遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#）

二叉树的反序列化(Deserialize)是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.temp_list = None

    def Serialize(self, root):
        if not root:
            return "#"
        return str(root.val) + "," + self.Serialize(root.left) + "," + self.Serialize(root.right)

    def Deserialize(self, s):
        if not s or s == "#,":
            return None
        self.temp_list = s.split(",")
        return self._func()

    def _func(self):
        if self.temp_list[0] == "#":
            self.temp_list = self.temp_list[1:]
            return None
        node = TreeNode(int(self.temp_list.pop(0)))
        node.left = self._func()
        node.right = self._func()
        return node
