# 给定一个无重复元素的整数数组nums，请你找出其中没有出现的最小的正整数 进阶： ;空间复杂度 ，时间复杂度 数据范围: 
#  Related Topics 数组 哈希 
# 示例:
# 输入:[1,0,2]
# 输出:3 
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class BM53minNumberDisappeared:
    def minNumberDisappeared(self, nums):
        nums.sort()
        temp_list = []
        # 过滤非正整数
        for val in nums:
            if val > 0:
                temp_list.append(val)
        # 最小值超过1，则返回最小正整数1
        if temp_list[0] > 1:
            return 1
        for i in range(len(temp_list) - 1):
            val = temp_list[i]
            if temp_list[i + 1] - val == 1:
                continue
            return temp_list[i] + 1
        # 列表中不缺少正整数，则结果为最后的列表值+1
        return temp_list[-1] + 1
