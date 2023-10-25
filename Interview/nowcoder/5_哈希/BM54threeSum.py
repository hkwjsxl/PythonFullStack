# 给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。 
#  数据范围：，数组中各个元素值满足 空间复杂度：，时间复杂度 
#  注意：
#  三元组（a、b、c）中的元素必须按非降序排列。（即a≤b≤c） 解集中不能包含重复的三元组。 例如，给定的数组 S = {-10 0 10 20 -10 
# -40},解集为(-10, -10, 20),(-10, 0, 10) 

#  Related Topics 数组 双指针 排序 
# 示例:
# 输入:[0]
# 输出:[]
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @return int整型二维数组
#
class BM54threeSum:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        if len(num) < 3:
            return []
        num.sort()
        last = len(num)
        res = []
        for i in range(last - 2):
            # 避免重复找同一个数据
            if i > 0 and num[i] == num[i - 1]:
                continue
            current_val = num[i]
            left = i + 1
            right = last - 1
            target_val = -current_val
            while left < right:
                if num[left] + num[right] > target_val:
                    right -= 1
                elif num[left] + num[right] < target_val:
                    left += 1
                else:
                    res.append([current_val, num[left], num[right]])
                    # 排除当前的两个值，往里面缩
                    left += 1
                    right -= 1
                    # 避免重复找
                    while left < right and num[left] == num[left - 1]:
                        left += 1
                    while left < right and num[right] == num[right + 1]:
                        right -= 1
        return res
