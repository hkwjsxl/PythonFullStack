"""二叉搜索树"""


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_recursion(val)

    def insert(self, node, data):
        if not self.root:
            node = BinaryTreeNode(data)
        elif data < node.data:
            node.lchild = self.insert(node.lchild, data)
            node.lchild.parent = node
        elif data > node.data:
            node.rchild = self.insert(node.rchild, data)
            node.rchild.parent = node
        return node

    def insert_no_recursion(self, data):
        node = self.root
        if not node:
            # 空树
            self.root = BinaryTreeNode(data)
            return
        while True:
            if data < node.data:
                if node.lchild:
                    node = node.lchild
                else:
                    node.lchild = BinaryTreeNode(data)
                    node.lchild.parent = node
                    return
            elif data > node.data:
                if node.rchild:
                    node = node.rchild
                else:
                    node.rchild = BinaryTreeNode(data)
                    node.rchild.parent = node
                    return
            else:
                # 不允许插入相同值
                return

    def query(self, node, data):
        if not node:
            return None
        if data < node.data:
            self.query(node.lchild, data)
        elif data > node.data:
            self.query(node.rchild, data)
        else:
            return node

    def query_no_recursion(self, data):
        node = self.root
        while node:
            if data < node.data:
                node = node.lchild
            elif data > node.data:
                node = node.rchild
            else:
                return node
        return None

    def __remove_node_1(self, node):
        # 情况1：如果要删除的节点是叶子节点：直接删除
        if node == node.parent.lchild:
            # 要删除的是左节点
            node.parent.lchild = None
        elif node == node.parent.rchild:
            # 要删除的是右节点
            node.parent.rchild = None
        else:
            # 只有一个节点(根节点)，直接删除根节点
            self.root = None

    def __remove_node_2_1(self, node):
        # 情况2.1：如果要删除的节点只有一个孩子（左孩子）：将此节点的父亲与孩子连接，然后删除该节点。
        if not node.parent:  # 根节点
            self.root = node.lchild
            node.lchild.parent = None  # 可有可无
        elif node == node.parent.lchild:  # 左结点
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:  # 右节点
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_2_2(self, node):
        # 情况2.1：如果要删除的节点只有一个孩子（右孩子）：将此节点的父亲与孩子连接，然后删除该节点。
        if not node.parent:  # 根节点
            self.root = node.rchild
            node.rchild.parent = None  # 可有可无
        elif node == node.parent.lchild:  # 左结点
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:  # 右节点
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, data):
        if self.root:
            # 不是空树
            node = self.query_no_recursion(data)
            if not node:
                # 节点不存在
                return False
            # 情况3：如果要删除的节点有两个孩子：将其右子树的最小节点（该节点最多有一个右孩子)删除，并替换当前节点。
            if not node.lchild and not node.rchild:
                # 只是一个叶子结点
                self.__remove_node_1(node)
            elif not node.rchild:
                # 只有左孩子，没有右孩子
                self.__remove_node_2_1(node)
            elif not node.lchild:
                # 只有右孩子，没有左孩子
                self.__remove_node_2_2(node)
            else:
                # 左右孩子都有
                tmp_node = node.rchild
                while tmp_node.lchild:
                    tmp_node = tmp_node.lchild
                node.data = tmp_node.data
                # 删除
                if tmp_node.rchild:
                    self.__remove_node_2_2(tmp_node)
                else:
                    self.__remove_node_1(tmp_node)
        else:
            return None

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)


tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
tree.in_order(tree.root)
print("\n------")
tree.delete(1)
tree.delete(3)
tree.delete(9)
tree.in_order(tree.root)
