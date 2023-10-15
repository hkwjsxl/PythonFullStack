# 给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径。
#  1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点 2.叶子节点是指没有子节点的节点 3.路径只能从父节点到子节点，不能从子节点到父节点 4
# .总节点数目为n 
#  例如：
#  给出如下的二叉树，，
#  
#  返回true，因为存在一条路径 的节点值之和为 22 
#  
#  数据范围： 1.树上的节点数满足 2.每 个节点的值都满足 
#  要求：空间复杂度 ，时间复杂度 进阶：空间复杂度 ，时间复杂度 
#  
#  Related Topics 树 dfs 
# 示例:
# 输入:{5,4,8,1,11,#,9,#,#,2,7},22
# 输出:true
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
# @param sum int整型 
# @return bool布尔型
#
class BM29hasPathSum:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
