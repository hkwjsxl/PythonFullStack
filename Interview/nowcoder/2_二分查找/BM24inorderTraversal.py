# 给定一个二叉树的根节点root，返回它的中序遍历结果。 数据范围：树上节点数满足 ，树上每个节点的值满足 进阶：空间复杂度 ，时间复杂度 
#  Related Topics 树 dfs 递归 广度优先搜索(BFS) 
# 示例:
# 输入:{1,2,#,#,3}
# 输出:[2,3,1] 
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
# @return int整型一维数组
#
class BM24inorderTraversal:
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
