# 给定一个长度为n的数组nums，请你找到峰值并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个所在位置即可。 1.峰值元素是指其值严格大于左右相
# 邻值的元素。严格大于即不能有等于 2.假设 nums[-1] = nums[n] = 3.对于所有有效的 i 都有 nums[i] != nums[i + 1]
#  4.你可以使用O(logN)的时间复杂度实现此问题吗？ 
#  数据范围： 
#  
#  
#  如输入[2,4,1,2,7,8,4]时，会形成两个山峰，一个是索引为1，峰值为4的山峰，另一个是索引为5，峰值为8的山峰，如下图所示： 
#  Related Topics 数组 查找 
# 示例:
# 输入:[2,4,1,2,7,8,4]
# 输出:1 
# 


# nowcoder submit region begin(Prohibit modification and deletion)
# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class BM19findPeakElement:
    def findPeakElement(self, nums):
        """
        峰值元素是指其值严格大于左右相邻值的元素。严格大于即不能有等于
        思路：
            由于题目中给出了“对于所有有效的 i 都有 nums[i] != nums[i + 1]”，就是相邻的不相等，所以直接二分就可以
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
