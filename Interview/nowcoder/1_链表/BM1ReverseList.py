# 给定一个单链表的头结点pHead(该头节点是有值的，比如在下图，它的val是1)，长度为n，
# 反转该链表后，返回新链表的表头。
#  数据范围： 要求：空间复杂度 ，时间复杂度 。 
#  如当输入链表{1,2,3}时， 经反转后，原链表变为{3,2,1}，所以对应的输出为{3,2,1}。 以上转换过程如下图所示：
#  Related Topics 链表 
# 示例:
# 输入:{1,2,3}
# 输出:{3,2,1}
#
# 示例2
# 输入：{}
# 返回值：{}
# 说明：
# 空链表则输出空


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
# @return ListNode类
#


class Solution:
    def ReverseList(self, head):
        if not head:
            return head
        else:
            current_head, prev_head, prev_head.next = head.next, head, None
            while current_head:
                temp_head, current_head.next = current_head.next, prev_head
                current_head, prev_head = temp_head, current_head
            return prev_head
