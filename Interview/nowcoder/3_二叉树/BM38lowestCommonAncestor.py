# 给定一棵二叉树(保证非空)以及这棵树上的两个节点对应的val值 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。 
#  数据范围：树上节点数满足 , 节点值val满足区间 [0,n) 要求：时间复杂度 
#  注：本题保证二叉树中每个节点的val值均不相同。 
#  如当输入{3,5,1,6,2,0,8,#,#,7,4},5,1时，二叉树{3,5,1,6,2,0,8,#,#,7,4}如下图所示： 所以节点值为5和节点值
# 为1的节点的最近公共祖先节点的节点值为3，所以对应的输出为3。
#  节点本身可以视为自己的祖先 
#  Related Topics 树 
# 示例:
# 输入:{3,5,1,6,2,0,8,#,#,7,4},5,1
# 输出:3
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
# @param root TreeNode类 
# @param o1 int整型 
# @param o2 int整型 
# @return int整型
#
class BM38lowestCommonAncestor:
    def lowestCommonAncestor(self, root, o1, o2):
        """在二叉树中找到两个节点的最近公共祖先"""
        if not root:
            return None
        if root.val == o1 or root.val == o2:
            return root.val
        left = self.lowestCommonAncestor(root.left, o1, o2)
        right = self.lowestCommonAncestor(root.right, o1, o2)
        if not left:
            return right
        if not right:
            return left
        # 左右子树都有，当前节点就是
        return root.val
