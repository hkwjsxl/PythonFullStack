# 给定一个链表，删除链表的倒数第 n 个节点并返回链表的头指针
#  例如， 给出的链表为: , .
#  删除了链表的倒数第 个节点之后,链表变为. 
#  数据范围： 链表长度 ，链表中任意节点的值满足 要求：空间复杂度 ，时间复杂度 
#  备注： 题目保证 一定是有效的
#  
#  Related Topics 链表 双指针 
# 示例:
# 输入:{1,2},2 
# 输出:{2} 
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
# @param n int整型 
# @return ListNode类
#
class BM9removeNthFromEnd:
    def removeNthFromEnd(self, head, n):
        """
        思路：链表值循环放入列表中，去除目标值后重新生成链表
        """
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next

        temp_list.pop(len(temp_list) - n)

        temp_node = ListNode(None)
        ret_node = temp_node
        for val in temp_list:
            temp_node.next = ListNode(val)
            temp_node = temp_node.next
        return ret_node.next
