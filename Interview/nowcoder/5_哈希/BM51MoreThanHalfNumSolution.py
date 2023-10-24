# 给一个长度为 n 的数组，数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。 例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。 
#  数据范围：，数组中元素的值 要求：空间复杂度：，时间复杂度 
#  Related Topics 哈希 数组 
# 示例:
# 输入:[1,2,3,2,2,2,5,4,2]
# 输出:2
# 


#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#
class BM51MoreThanHalfNumSolution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        temp_dict = {}
        for val in numbers:
            temp_dict[val] = temp_dict.get(val, 0) + 1
        res = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
        print(res)
        return res[0][0]
