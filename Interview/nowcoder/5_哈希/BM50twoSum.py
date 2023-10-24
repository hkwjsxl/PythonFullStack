# 给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。 （注：返回的数组下标从1
# 开始算起，保证target一定可以由数组里面2个数字相加得到） 
#  数据范围：，， 要求：空间复杂度 ，时间复杂度 
#  Related Topics 数组 哈希 
# 示例:
# 输入:[3,2,4],6
# 输出:[2,3]
# 


#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @param target int整型 
# @return int整型一维数组
#
class BM50twoSum:
    def twoSum(self , numbers: List[int], target: int) -> List[int]:
        """
        思路：
            目标值减去列表中的值，看得到的数字是否在列表中
        """
        temp_dict = {}
        for i in range(len(numbers)):
            if target - numbers[i] in temp_dict:
                return [temp_dict[target - numbers[i]],i+1]
            else:
                temp_dict[numbers[i]] = i+1
