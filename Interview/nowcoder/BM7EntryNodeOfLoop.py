# 给一个长度为n链表，若其中包含环，请找出该链表的环的入口结点，否则，返回null。 
#  数据范围： ， 要求：空间复杂度 ，时间复杂度 
#  例如，输入{1,2},{3,4,5}时，对应的环形链表如下图所示： 
#  可以看到环的入口结点的结点值为3，所以返回结点值为3的结点。
#  
#  Related Topics 链表 哈希 双指针 
# 示例:
# 输入:{1,2},{3,4,5}
# 输出:3
# 


# nowcoder submit region begin(Prohibit modification and deletion)
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class BM7EntryNodeOfLoop:
    def EntryNodeOfLoop(self, pHead):
        temp_list = []
        while pHead:
            if pHead in temp_list:
                return pHead
            temp_list.append(pHead)
            pHead = pHead.next
        return None
