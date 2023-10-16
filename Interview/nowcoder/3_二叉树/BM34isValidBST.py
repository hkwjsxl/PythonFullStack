# 给定一个二叉树根节点，请你判断这棵树是不是二叉搜索树。 
#  二叉搜索树满足每个节点的左子树上的所有节点均小于当前节点且右子树上的所有节点均大于当前节点。 
#  例： 图1 
#  图2 
#  数据范围：节点数量满足 ，节点上的值满足 
#  
#  Related Topics 树 
# 示例:
# 输入:{1,2,3}
# 输出:false 
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
# @return bool布尔型
#
class BM34isValidBST:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        lst = self._func(root)
        if lst == sorted(lst):
            return True
        return False

    def _func(self, root):
        # 中序遍历
        if not root:
            return []
        return self._func(root.left) + [root.val] + self._func(root.right)
