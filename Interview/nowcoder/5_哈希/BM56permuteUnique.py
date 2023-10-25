# 给出一组可能包含重复项的数字，返回该组数字的所有排列。结果以字典序升序排列。 
#  数据范围： ，数组中的值满足 
#  要求：空间复杂度 ，时间复杂度 
#  Related Topics 递归 
# 示例:
# 输入:[1,1,2]
# 输出:[[1,1,2],[1,2,1],[2,1,1]]
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @return int整型二维数组
#
class BM56permuteUnique:
    def permuteUnique(self, num):
        """有重复项数字的全排列"""
        if len(num) <= 1:
            return [num]
        num.sort()
        res = []
        for index, value in enumerate(num):
            temp = self.permuteUnique(num[:index] + num[index + 1:])
            val = [[value] + i for i in temp]
            res += [j for j in val if j not in res]
        return res
