# 请根据二叉树的前序遍历，中序遍历恢复二叉树，并打印出二叉树的右视图 
#  数据范围： 
#  要求： 空间复杂度 ，时间复杂度 
#  
#  如输入[1,2,4,5,3],[4,2,5,1,3]时，通过前序遍历的结果[1,2,4,5,3]和中序遍历的结果[4,2,5,1,3]可重建出以下二叉树：
#  
#  所以对应的输出为[1,3,5]。 
#  Related Topics 树 
# 示例:
# 输入:[1,2,4,5,3],[4,2,5,1,3]
# 输出:[1,3,5] 
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 求二叉树的右视图
# @param preOrder int整型一维数组 先序遍历
# @param inOrder int整型一维数组 中序遍历
# @return int整型一维数组
#
class BM41solve:
    def solve(self, preOrder: List[int], inOrder: List[int]) -> List[int]:
        """
        输出二叉树的右视图---前序遍历，中序遍历恢复二叉树，并打印出二叉树的右视图
        """
        root = self.re_construct_binary_tree(preOrder, inOrder)
        return self._right_view(root)

    def re_construct_binary_tree(self, preOrder, inOrder):
        if not preOrder or not inOrder:
            return None
        node = TreeNode(preOrder[0])
        mid = inOrder.index(preOrder[0])
        node.left = self.re_construct_binary_tree(preOrder[1:mid + 1], inOrder[:mid])
        node.right = self.re_construct_binary_tree(preOrder[mid + 1:], inOrder[mid + 1:])
        return node

    def _right_view(self, root):
        temp_list = [root]
        res = []
        while temp_list:
            res.append(temp_list[-1].val)
            for _ in range(len(temp_list)):
                node = temp_list.pop(0)
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
        return res
