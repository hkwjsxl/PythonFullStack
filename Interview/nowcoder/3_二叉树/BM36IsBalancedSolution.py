# 输入一棵节点数为 n 二叉树，判断该二叉树是否是平衡二叉树。 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树 平衡二叉树（Balanced 
# Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
#  样例解释： 样例二叉树如图，为一颗平衡二叉树
#  注：我们约定空树是平衡二叉树。 
#  数据范围：,树上节点的val值满足 要求：空间复杂度，时间复杂度 
#  Related Topics 树 dfs 
# 示例:
# 输入:{1,2,3,4,5,6,7}
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
# @param pRoot TreeNode类 
# @return bool布尔型
#
class BM36IsBalancedSolution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        if abs(self._max_depth(pRoot.left) - self._max_depth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def _max_depth(self, root):
        # 最大深度
        if not root:
            return 0
        return max(self._max_depth(root.left), self._max_depth(root.right)) + 1
