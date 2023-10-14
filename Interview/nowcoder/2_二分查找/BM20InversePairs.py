# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。
# 即输出P mod 1000000007 数据范围： ; 对于 的数据, 对于 的数据, 数组中所有数字的值满足 要求：空间复杂度 ，时间复杂度
# 输入描述：
# 题目保证输入的数组中没有相同的数字
#  Related Topics 数组 
# 示例:
# 输入:[1,2,3,4,5,6,7,0]
# 输出:7
# 

class BM20InversePairs:
    """
    输入: arr[]={8，5，4，2，1}
    输出: 10
    解释: 逆序对为(8，5)、(8，4)、(8，2)、(8，1)，(5，4)、(5，2)、(5，1)，还有(4，2)、(4，1)和(2，1)，总共10个。
    其实也可以直接计算5(5-1)/2=10，前提是知道数组完全逆序
    完善正序的列表就是0个逆序对
    """

    def InversePairs(self, nums):
        return self._recur(nums) % 1000000007

    def _recur(self, nums):
        if len(nums) <= 1: return 0
        a, b = [], []
        res = 0
        prev_val = nums[0]
        for val in nums[1:]:
            if val > prev_val:
                a.append(val)
            else:
                b.append(val)
                res += len(a) + 1
            print(a,b)
        return res + self._recur(a) + self._recur(b)


# print(BM20InversePairs().InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
print(BM20InversePairs().InversePairs([8, 5, 4, 2, 1]))
