# 有一个长度为 n 的非降序数组，比如[1,2,3,4,5]，将它进行旋转，
# 即把一个数组最开始的若干个元素搬到数组的末尾，变成一个旋转数组，比如变成了[3,4,5,1,2]，或者[4,5,1,2,3]这样的。
# 请问，给定这样一个旋转数组，求数组中的最小值。
#  
#  数据范围：，数组中任意元素的值: 要求：空间复杂度： ，时间复杂度： 
#  Related Topics 二分 
# 示例:
# 输入:[3,4,5,1,2]
# 输出:1
# 


class BM21minNumberInRotateArray:
    def minNumberInRotateArray(self, nums):
        # 方式一：min函数
        # return min(nums)
        # 方式二：二分
        left, right = 0, len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[mid]
