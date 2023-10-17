# 给定节点数为 n 的二叉树的前序遍历和中序遍历结果，请重建出该二叉树并返回它的头结点。 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列
# {4,7,2,1,5,3,8,6}，则重建出如下图所示。 
#  
#  提示: 1.vin.length == pre.length 2.pre 和 vin 均无重复元素 3.vin出现的元素均出现在 pre里 4.只需要返回
# 根结点，系统会自动输出整颗树做答案对比 数据范围：，节点的值 要求：空间复杂度 ，时间复杂度 
#  Related Topics 树 dfs 数组 
# 示例:
# 输入:[1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]
# 输出:{1,2,3,4,#,5,6,#,7,#,#,8}
# 


# coding:utf-8
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param preOrder int整型一维数组 
# @param vinOrder int整型一维数组 
# @return TreeNode类
#
class BM40reConstructBinaryTree:
    def reConstructBinaryTree(self, preOrder: List[int], vinOrder: List[int]) -> TreeNode:
        """
        重构二叉树---有前序和中序，求整棵树
            1.找出前序遍历中第一个值，即根节点，并记录它在中序遍历中的位置。
            2.根据根节点，将中序遍历分为左子树中序遍历和右子树中序遍历。
            3.判断子树的前、中序遍历是否为空，是返回None，否递归调用1,2步。
        """
        # if len(vinOrder) == 0:
        #     return None
        # node = TreeNode(preOrder.pop(0))  # 第一个节点为根
        # mid = vinOrder.index(node.val)
        # # 分为左子树中序遍历和右子树中序遍历
        # node.left = self.reConstructBinaryTree(preOrder, vinOrder[:mid])
        # node.right = self.reConstructBinaryTree(preOrder, vinOrder[mid + 1:])
        # return node
        if len(preOrder) == 0 or len(vinOrder) == 0:
            return None
        # 第一个节点为根
        node = TreeNode(preOrder[0])
        temp = vinOrder.index(preOrder[0])
        # 分为左子树中序遍历和右子树中序遍历
        node.left = self.reConstructBinaryTree(preOrder[1:temp + 1], vinOrder[:temp])
        node.right = self.reConstructBinaryTree(preOrder[temp + 1:], vinOrder[temp + 1:])
        return node
