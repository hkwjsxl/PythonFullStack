# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。 
#  数据范围：二叉树的节点数量满足 ，二叉树节点的值满足 ，树的各节点的值各不相同 示例 1： 
#  
#  Related Topics 树 递归 dfs 广度优先搜索(BFS) 
# 示例:
# 输入:{1,#,2,3}
# 输出:[1,2,3] 
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
class BM23preorderTraversal:
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
