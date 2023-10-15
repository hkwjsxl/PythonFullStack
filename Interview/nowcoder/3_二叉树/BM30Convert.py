# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。如下图所示 
#  
#  数据范围：输入二叉树的节点数 ，二叉树中每个节点的值 
#  要求：空间复杂度（即在原树上操作），时间复杂度 
#  
#  注意: 1.要求不能创建任何新的结点，只能调整树中结点指针的指向。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继
#  2.返回链表中的第一个节点的指针
#  3.函数返回的TreeNode，有左右指针，其实可以看成一个双向链表的数据结构 4.你不用输出双向链表，程序会根据你的返回值自动打印输出 
#  Related Topics 分治 
# 示例:
# 输入:{10,6,14,4,8,12,16}
# 输出:From left to right are:4,6,8,10,12,14,16;From right to left are:16,14,12,10
# ,8,6,4;
# 


# nowcoder submit region begin(Prohibit modification and deletion)
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 方式一
class BM30Convert:
    def Convert(self, pRootOfTree):
        # 利用二叉搜索树的性质中序遍历递归
        if not pRootOfTree:
            return None

        # 左子树
        left = self.Convert(pRootOfTree.left)
        temp = left
        # 定位到左子树的最右节点
        while left and temp.right:
            temp = temp.right
        # 绑定双向链表
        if left:
            temp.right = pRootOfTree
            pRootOfTree.left = temp

        # 右子树
        right = self.Convert(pRootOfTree.right)
        if right:
            pRootOfTree.right = right
            right.left = pRootOfTree

        return left or pRootOfTree


# 方式二
class BM30Convert:
    def __init__(self):
        self.ret = None
        self.temp = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        # 左
        self.Convert(pRootOfTree.left)
        # 中
        if not self.ret:
            # 初始化
            self.ret = pRootOfTree
            self.temp = pRootOfTree
        else:
            # 链接
            self.temp.right = pRootOfTree
            pRootOfTree.left = self.temp
            self.temp = pRootOfTree
        # 右
        self.Convert(pRootOfTree.right)
        return self.ret
