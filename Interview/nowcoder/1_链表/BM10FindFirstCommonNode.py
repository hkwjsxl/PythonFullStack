# 输入两个无环的单向链表，找出它们的第一个公共结点，如果没有公共节点则返回空。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据
# 是正确的） 
#  数据范围： 
#  要求：空间复杂度 ，时间复杂度 
#  
#  例如，输入{1,2,3},{4,5},{6,7}时，两个无环的单向链表的结构如下图所示： 
#  可以看到它们的第一个公共结点的结点值为6，所以返回结点值为6的结点。 
#  Related Topics 链表 
# 示例:
# 输入:{1,2,3},{4,5},{6,7}
# 输出:{6,7}
# 


# nowcoder submit region begin(Prohibit modification and deletion)
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class BM10FindFirstCommonNode:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        思路：将第一个链表循环放入列表，循环第二个链表，如果节点已存在直接返回
        """
        temp_list = []
        while pHead1:
            temp_list.append(pHead1)
            pHead1 = pHead1.next

        while pHead2:
            if pHead2 in temp_list:
                return pHead2
            pHead2 = pHead2.next
        return None
