# 请实现无重复数字的升序数组的二分查找 
#  给定一个 元素升序的、无重复数字的整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标（
# 下标从 0 开始），否则返回 -1 
#  数据范围： ， 数组中任意值满足 进阶：时间复杂度 ，空间复杂度 
#  
#  Related Topics 二分 
# 示例:
# 输入:[-1,0,3,4,6,10,13,14],13
# 输出:6 
# 


# nowcoder submit region begin(Prohibit modification and deletion)
# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#
class BM17search:
    def search(self, nums, target):
        if not nums:
            return -1
        try:
            return nums.index(target)
        except:
            return -1
