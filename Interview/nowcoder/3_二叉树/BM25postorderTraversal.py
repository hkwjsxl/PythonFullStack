# 给定一个二叉树，返回他的后序遍历的序列。 
#  后序遍历是值按照 左节点->右节点->根节点 的顺序的遍历。 
#  数据范围：二叉树的节点数量满足 ，二叉树节点的值满足 ，树的各节点的值各不相同
#  
#  样例图 
#  
#  Related Topics 树 递归 dfs 广度优先搜索(BFS) 
# 示例:
# 输入:{1,#,2,3}
# 输出:[3,2,1] 
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
class BM25postorderTraversal:
    def postorderTraversal(self, root):
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
