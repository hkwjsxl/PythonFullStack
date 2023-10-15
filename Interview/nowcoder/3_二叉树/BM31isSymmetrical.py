# 给定一棵二叉树，判断其是否是自身的镜像（即：是否对称）
#  例如： 下面这棵二叉树是对称的
#  
#  下面这棵二叉树不对称。
#  
#  数据范围：节点数满足 ，节点上的值满足 要求：空间复杂度 ，时间复杂度 备注： 你可以用递归和迭代两种方法解决这个问题 
#  Related Topics 树 
# 示例:
# 输入:{1,2,2,3,4,4,3}
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
class BM31isSymmetrical:
    def isSymmetrical(self, pRoot):
        """
        分析：
            递归-两种情况：
            1.根节点以及其左右子树，左子树的左子树和右子树的右子树相同
            2.左子树的右子树和右子树的左子树相同
        """
        if not pRoot:
            return True
        return self._func(pRoot.left, pRoot.right)

    def _func(self, left, right):
        # 比较函数
        if not left:
            return right is None
        if not right:
            return False
        if left.val != right.val:
            return False
        return self._func(left.left, right.right) and self._func(left.right, right.left)
