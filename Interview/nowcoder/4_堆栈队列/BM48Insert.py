# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数
# 值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。 
#  数据范围：数据流中数个数满足 ，大小满足 
#  
#  进阶： 空间复杂度 ， 时间复杂度 
#  
#  Related Topics 排序 堆 
# 示例:
# 输入:[5,2,3,4,1,6,7,0,8]
# 输出:"5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00 "
# 


# -*- coding:utf-8 -*-
class BM48Insert:
    def __init__(self):
        self.temp_list = []

    def Insert(self, num):
        self.temp_list.append(num)

    def GetMedian(self):
        self.temp_list.sort()
        l = len(self.temp_list) - 1
        if l % 2 == 1:
            return (self.temp_list[l // 2] + self.temp_list[l // 2 + 1]) / 2
        return self.temp_list[l // 2]
