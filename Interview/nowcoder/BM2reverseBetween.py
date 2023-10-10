# 将一个节点数为 size 链表 m 位置到 n 位置之间的区间反转，要求时间复杂度 ，空间复杂度 。
#  例如：
#  给出的链表为 , ,
#  返回 .
#  
#  数据范围： 链表长度 ，，链表中每个节点的值满足 要求：时间复杂度 ，空间复杂度 进阶：时间复杂度 ，空间复杂度 
#  Related Topics 链表 
# 示例:
# 输入:{1,2,3,4,5},2,4
# 输出:{1,4,3,2,5}
# 

# nowcoder submit region begin(Prohibit modification and deletion)
# coding:utf-8
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param m int整型 
# @param n int整型 
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        temp_list = [0, head]  # 0是占位符，方便下面取元素
        while temp_list[-1].next:
            temp_list.append(temp_list[-1].next)
        while m <= n:
            temp_list[m].val, temp_list[n].val = temp_list[n].val, temp_list[m].val
            m += 1
            n -= 1
        return head
