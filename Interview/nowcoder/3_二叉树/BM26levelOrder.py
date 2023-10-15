# 给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
#  例如：
#  给定的二叉树是{3,9,20,#,#,15,7},
#  
#  该二叉树层序遍历的结果是
#  [
#  [3],
#  [9,20],
#  [15,7] ] 
#  
#  提示: 0 <= 二叉树的结点数 <= 1500 
#  
#  
#  Related Topics 树 广度优先搜索(BFS) 
# 示例:
# 输入:{1,2}
# 输出:[[1],[2]] 
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
# @return int整型二维数组
#
# 方式一
# class BM26levelOrder:
#     def __init__(self):
#         self.res = []
#
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         self._func(root, 0)
#         return self.res
#
#     def _func(self, root, index):
#         if not root:
#             return
#         if len(self.res) <= index:
#             self.res.append([root.val])
#         else:
#             self.res[index].append(root.val)
#         index += 1
#         if root.left:
#             self._func(root.left, index)
#         if root.right:
#             self._func(root.right, index)

# 方式二
class BM26levelOrder:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        temp_list = [root]
        res = []
        while temp_list:
            row_list = []
            for i in range(len(temp_list)):
                node = temp_list.pop(0)
                row_list.append(node.val)
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            res.append(row_list)
        return res
