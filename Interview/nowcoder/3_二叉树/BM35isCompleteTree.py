# 给定一个二叉树，确定他是否是一个完全二叉树。 
#  完全二叉树的定义：若二叉树的深度为 h，除第 h 层外，其它各层的结点数都达到最大个数，第 h 层所有的叶子结点都连续集中在最左边，这就是完全二叉树。（第
#  h 层可能包含 [1~2h] 个节点）
#  
#  数据范围：节点数满足 
#  样例图1： 样例图2： 样例图3： 
#  
#  Related Topics 树 dfs 广度优先搜索(BFS) 
# 示例:
# 输入:{1,2,3,4,5,6}
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
# @return bool布尔型
#
class BM35isCompleteTree:
    def isCompleteTree(self, root):
        if not root:
            return True
        ret = [root]
        while ret:
            node = ret.pop(0)
            if node:
                ret.append(node.left)
                ret.append(node.right)
            else:
                break
        for node in ret:
            if node:
                return False
        return True
