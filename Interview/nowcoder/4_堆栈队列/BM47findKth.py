# 有一个整数数组，请你根据快速排序的思路，找出数组中第 k 大的数。 给定一个整数数组 a ,同时给定它的大小n和要找的 k ，请返回第 k 大的数(包括重复
# 的元素，不用去重)，保证答案存在。 要求：时间复杂度 ，空间复杂度 数据范围：， ，数组中每个元素满足 
#  Related Topics 堆 分治 
# 示例:
# 输入:[1,3,5,2,2],5,3 
# 输出:2 
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
class BM47findKth:
    def findKth(self, a: List[int], n: int, K: int) -> int:
        """寻找第K大"""
        return self._quick_sort(a)[K - 1]

    def _quick_sort(self, lst):
        if len(lst) <= 1:
            return lst
        left_list = []
        current_list = []
        right_list = []
        temp_val = lst[0]
        for val in lst:
            if val < temp_val:
                left_list.append(val)
            elif val > temp_val:
                right_list.append(val)
            else:
                current_list.append(val)
        return self._quick_sort(right_list) + current_list + self._quick_sort(left_list)
