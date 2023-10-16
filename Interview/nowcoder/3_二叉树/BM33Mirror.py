# 操作给定的二叉树，将其变换为源二叉树的镜像。 数据范围：二叉树的节点数 ， 二叉树每个节点的值 要求： 空间复杂度 。本题也有原地操作，即空间复杂度 的解法
# ，时间复杂度 
#  比如： 源二叉树
#  镜像二叉树 
#  
#  Related Topics 树 
# 示例:
# 输入:{8,6,10,5,7,9,11}
# 输出:{8,10,6,11,9,7,5}
# 


# nowcoder submit region begin(Prohibit modification and deletion)
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
# @param pRoot TreeNode类 
# @return TreeNode类
#
class BM33Mirror:
    def Mirror(self, pRoot):
        if pRoot:
            left = self.Mirror(pRoot.right)
            right = self.Mirror(pRoot.left)
            pRoot.left = left
            pRoot.right = right
            return pRoot
