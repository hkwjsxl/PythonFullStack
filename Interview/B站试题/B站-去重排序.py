"""
给定一个升序排列的的长度为 n 的数组 nums，数组中每个元素都是正整数，
请删除一部分这个数组的重复元素(数组元素需要原地改变)，
让这个数组中的每个数字都严格大于前一个数（第一个数除外），
然后返回删除过后该数组的长度。
假设你返回长度是 m。如果 m 是正确答案，修改后的数组 nums 有 m 或 m 个以上个元素，并且前 m 个元素符合要求，那么你的代码将被判为正确。

例如n=4，nums=[1,2,2,3]，则输出3。
例如n=5，nums=[1,1,22,30,41]，则输出4。


"""


class Solution:
    def del_repeat_item(self, n: int, nums) -> int:
        for i in range(n - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                nums.pop(i)
        return len(nums)


ret = Solution().del_repeat_item(4, [1, 2, 2, 3])
print(ret)
