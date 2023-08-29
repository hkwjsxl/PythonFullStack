"""
输入一个正整数数组，将它们连接起来排成一个数，输出能排出的所有数字中最小的一个。

解决这个问题可以采用贪心算法，具体步骤如下：
将输入的数组转化为字符串数组。
对字符串数组进行排序，排序规则为字符串拼接后结果小的在前。
将排序后的字符串数组依次拼接起来，得到最终结果。
其中，排序规则中x + x[0] * (9 - len(x))的含义是将字符串x拼接成长度为9的字符串，使得比较时不受字符串长度影响。
例如，对于字符串'10'来说，拼接后为'101010101'。
"""


class Solution:
    def smallest_num(self, nums):
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=lambda x: x + x[0] * (9 - len(x)))  # 排序规则
        return ''.join(nums_str)


nums = [10, 2, 5]
ret = Solution().smallest_num(nums)
print(ret)
