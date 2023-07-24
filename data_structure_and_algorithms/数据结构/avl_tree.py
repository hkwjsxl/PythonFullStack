class AVLNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None
        self.bf = 0  # balance factor


class AVL:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_recursion(val)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    def perv_order(self, root):
        if root:
            print(root.data, end=",")
            self.perv_order(root.lchild)
            self.perv_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")

    def rotate_left(self, p, c):
        """
        左旋
        :param p: 节点
        :param c: 节点
        :return:
        """
        s2 = c.lchild
        p.rchild = s2
        if s2:
            # s2不存在时，None没有parent属性
            s2.parent = p
        c.lchild = p
        p.parent = c
        # 设置balance factor
        p.bf = 0
        c.bf = 0
        # 返回根节点
        return c

    def rotate_right(self, p, c):
        # 右旋
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        """先右旋再左旋"""

        # 旋转后的根节点
        g = c.lchild

        # 旋转要动的节点（右旋）
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        # 旋转要动的节点（左旋）
        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # bf的三种情况（左边沉标记为-1，右边沉标记为1，平衡是0）
        if g.bf < 0:
            # 左边沉
            p.bf = 0
            c.bf = 1
        elif g.bf > 0:
            # 右边沉
            p.bf = -1
            c.bf = 0
        else:
            # s1,s2,s3,s4都是空
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def rotate_left_right(self, p, c):
        """先左旋再右旋"""

        # 旋转后的根节点
        g = c.rchild

        # 旋转要动的节点（左旋）
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        # 旋转要动的节点（右旋）
        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # bf的三种情况
        if g.bf < 0:
            c.bf = 0
            p.bf = 1
        elif g.bf > 0:
            c.bf = -1
            p.bf = 0
        else:
            c.bf = 0
            p.bf = 0
        g.bf = 0
        return g

    def insert_no_recursion(self, data):
        # 插入
        node = self.root
        if not node:
            self.root = AVLNode(data)
            return
        while True:
            if data < node.data:
                if node.lchild:
                    node = node.lchild
                else:
                    node.lchild = AVLNode(data)
                    node.lchild.parent = node
                    insert_node = node.lchild  # 当前插入的节点
                    break
            elif data > node.data:
                if node.rchild:
                    node = node.rchild
                else:
                    node.rchild = AVLNode(data)
                    node.rchild.parent = node
                    insert_node = node.rchild  # 当前插入的节点
                    break
            else:
                # 不允许插入相同值
                return
        # 更新bf
        while insert_node.parent:
            if insert_node.parent.lchild == insert_node:
                # 如果是从左边上来的，左边就更沉了
                # 两种情况：左边的左孩子（右旋）；左边的右孩子（左旋-右旋）
                # 更新insert_node.parent.bf-=1
                if insert_node.parent.bf < 0:  # 原来是-1，更新后变为-2
                    m = insert_node.parent.parent  # 为了下面的链接
                    x = insert_node.parent  # 旋转后的parent会改变，所以要记录一下
                    if insert_node.bf < 0:
                        # 左边的左孩子
                        n = self.rotate_right(insert_node.parent, insert_node)
                    else:  # bf为0时，不会再往上传，所以不可能等于0，只有大于小于两种情况
                        # 左边的右孩子
                        n = self.rotate_left_right(insert_node.parent, insert_node)
                elif insert_node.parent.bf > 0:  # 原来是1，更新后变为0
                    insert_node.parent.bf = 0
                    break  # bf为0时，树的高度没有发生变化，所以不会影响原来的bf，直接退出循环
                else:  # 原来是0，更新后变为-1
                    insert_node.parent.bf = -1
                    insert_node = insert_node.parent
                    continue  # 满足绝对值不大于2，继续
            else:
                # 如果是从右边上来的，右边就更沉了
                # 两种情况：右边的左孩子（右旋-左旋）；右边的右孩子（左旋）
                # 更新insert_node.parent.bf+=1
                if insert_node.parent.bf < 0:  # 原来是-1，更新后是0
                    insert_node.parent.bf = 0
                    break  # bf为0时，树的高度没有发生变化，所以不会影响原来的bf，直接退出循环
                elif insert_node.parent.bf > 0:  # 原来是1，更新后变为2
                    m = insert_node.parent.parent  # 为了下面的链接
                    x = insert_node.parent  # 旋转后的parent会改变，所以要记录一下
                    if insert_node.bf < 0:
                        n = self.rotate_right_left(insert_node.parent, insert_node)
                    else:  # bf为0时，不会再往上传，所以不可能等于0，只有大于小于两种情况
                        n = self.rotate_left(insert_node, insert_node)
                else:  # 原来是0，更新后变为1
                    insert_node.parent.bf = 1
                    insert_node = insert_node.parent
                    continue  # 满足绝对值不大于2，继续

            # 链接旋转后的子树
            n.parent = m
            if m:
                if x == m.lchild:
                    m.lchild = n
                else:
                    m.rchild = n
            else:
                self.root = n
            break


tree = AVL([9, 8, 7, 6, 5, 4, 3, 2, 1])

tree.perv_order(tree.root)
print("")
tree.in_order(tree.root)
