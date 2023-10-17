# 给定一个长度为 n 的数组 num 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。 
#  例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组
# {2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2
# ,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。 
#  窗口大于数组长度或窗口长度为0的时候，返回空。
#  
#  数据范围： ，，数组中每个元素的值满足 要求：空间复杂度 ，时间复杂度 
#  
#  
#  Related Topics 堆 双指针 队列 
# 示例:
# 输入:[2,3,4,2,6,2,5,1],3
# 输出:[4,4,6,6,6,5]
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @param size int整型 
# @return int整型一维数组
#
class BM45maxInWindows:
    def maxInWindows(self, num, size):
        """
        滑动窗口的最大值
        """
        if size > len(num):
            return []
        if size == 0:
            return []
        res_list = []
        for i in range(len(num) - size + 1):
            temp_list = num[i:i + size]
            max_val = max(temp_list)
            res_list.append(max_val)
        return res_list
