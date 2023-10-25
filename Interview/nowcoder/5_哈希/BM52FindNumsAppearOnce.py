# 一个整型数组里除了两个数字只出现一次，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。 
#  数据范围：数组长度 ，数组中每个数的大小 
#  要求：空间复杂度 ，时间复杂度 
#  
#  提示：输出时按非降序排列。 
#  Related Topics 位运算 哈希 
# 示例:
# 输入:[1,4,1,6]
# 输出:[4,6]
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型一维数组
#
class BM52FindNumsAppearOnce:
    def FindNumsAppearOnce(self, nums):
        temp_dict = {}
        for val in nums:
            temp_dict[val] = temp_dict.get(val, 0) + 1
        res = []
        for key, value in temp_dict.items():
            if value == 1:
                res.append(key)
        res.sort()
        return res
