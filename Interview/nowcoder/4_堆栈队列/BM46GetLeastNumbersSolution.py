# 给定一个长度为 n 的可能有重复值的数组，找出其中不去重的最小的 k 个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2
# ,3,4(任意顺序皆可)。 数据范围：，数组中每个数的大小 要求：空间复杂度 ，时间复杂度 
#  Related Topics 堆 排序 分治 
# 示例:
# 输入:[4,5,1,6,2,7,3,8],4 
# 输出:[1,2,3,4]
# 

# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param input int整型一维数组 
# @param k int整型 
# @return int整型一维数组
#
class BM46GetLeastNumbersSolution:
    def GetLeastNumbers_Solution(self , input: List[int], k: int) -> List[int]:
        """最小的K个数"""
        res = []
        while len(res) < k:
            min_val = min(input)
            res.append(min_val)
            input.remove(min_val)
        return res
