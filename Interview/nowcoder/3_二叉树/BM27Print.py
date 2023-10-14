# 给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替） 
#  数据范围：,树上每个节点的val满足 
#  要求：空间复杂度：，时间复杂度： 例如：
#  给定的二叉树是{1,2,3,#,#,4,5}
#  
#  该二叉树之字形层序遍历的结果是 [ [1], [3,2], [4,5] ] 
#  Related Topics 栈 树 队列 
# 示例:
# 输入:{1,2,3,#,#,4,5}
# 输出:[[1],[3,2],[4,5]]
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
# @return int整型二维数组
#
class BM27Print:
    def Print(self, pRoot: TreeNode) -> List[List[int]]:
        if not pRoot:
            return []
        temp_list = [pRoot]
        res = []
        flag = False
        while temp_list:
            row_list = []
            for i in range(len(temp_list)):
                node = temp_list.pop(0)
                row_list.append(node.val)
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            flag = not flag
            if flag:
                res.append(row_list)
            else:
                res.append(row_list[::-1])
        return res
