"""两数之和等于所给定的数"""


# 方法一
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    执行耗时:3584 ms,击败了7.15% 的Python用户
	内存消耗:13.6 MB,击败了84.58% 的Python用户
    """
    for i in range(len(nums)):
        j = i + 1
        while j <= len(nums) - 1:
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1


# 方法二
def twoSum(nums, target):
    """
    后面的数以此从前往后比较
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    执行耗时:268 ms,击败了65.69% 的Python用户
	内存消耗:13.4 MB,击败了97.51% 的Python用户
    """
    i = 0
    j = len(nums) - 1
    while i < j:
        while i < j:
            if nums[i] + nums[j] == target:
                return [i, j]
            i += 1
        j -= 1
        i = 0


print(twoSum([3, 3, 2], 6))
print(twoSum([3, 2, 3], 6))
print(twoSum([3, 2, 4], 6))
