# 给出一组数字，返回该组数字的所有排列 例如： [1,2,3]的所有排列如下
#  [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2], [3,2,1].
#  （以数字在数组中的位置靠前为优先级，按字典序排列输出。） 
#  数据范围：数字个数 要求：空间复杂度 ，时间复杂度 
#  Related Topics 递归 
# 示例:
# 输入:[1,2,3]
# 输出:[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @return int整型二维数组
#
class BM55permute:
    def permute(self, num: List[int]) -> List[List[int]]:
        """没有重复项数字的全排列"""
        if len(num) <= 1:
            return [num]
        ret = []
        for index, value in enumerate(num):
            temp = self.permute(num[:index] + num[index + 1:])
            ret += [[value] + i for i in temp]
        return ret
