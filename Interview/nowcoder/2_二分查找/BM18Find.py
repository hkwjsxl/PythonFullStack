# 在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个
# 二维数组和一个整数，判断数组中是否含有该整数。
#  [
#   [1,2,8,9],
#   [2,4,9,12],
#   [4,7,10,13],
#   [6,8,11,15]
#  ] 给定 target = 7，返回 true。 给定 target = 3，返回 false。 
#  数据范围：矩阵的长宽满足 ， 矩阵中的值满足 
#  进阶：空间复杂度 ，时间复杂度 
#  
#  Related Topics 数组 
# 示例:
# 输入:7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
# 输出:true
# 


# nowcoder submit region begin(Prohibit modification and deletion)
# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param target int整型 
# @param array int整型二维数组 
# @return bool布尔型
#
class BM18Find:
    def Find(self, target, array):
        """
        思路：
            * 矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，
            * 因此从左下角开始查找，当要查找数字比左下角数字大时。右移
            * 要查找数字比左下角数字小时，上移
        """
        if not array:
            return False
        if not array[-1]:
            return False
        i = len(array) - 1
        j = 0
        while j < len(array[-1]) and i > -1:
            current_value = array[i][j]
            if target < current_value:
                i -= 1
            elif target > current_value:
                j += 1
            else:
                return True
        return False
