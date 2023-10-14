# 给出一个升序排序的链表，删除链表中的所有重复出现的元素，只保留原链表中只出现一次的元素。
#  例如：
#  给出的链表为, 返回.
#  给出的链表为, 返回. 
#  数据范围：链表长度 ，链表中的值满足 要求：空间复杂度 ，时间复杂度 进阶：空间复杂度 ，时间复杂度 
#  Related Topics 链表 
# 示例:
# 输入:{1,2,2}
# 输出:{1}
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
# @return ListNode类
#
class BM16deleteDuplicates:
    def deleteDuplicates(self, head):
        """
        思路：
            比较当前值与后一个值，不相等则跟在新链表后面，
            相等就存储当前值，链表依次往后走，直到值不相等
        """
        if not head:
            return head
        ret_node = temp_node = ListNode(None)
        while head and head.next:
            if head.val != head.next.val:
                temp_node.next = head
                temp_node = temp_node.next
                head = head.next
            else:
                temp_val = head.val
                while head and head.val == temp_val:
                    head = head.next
        temp_node.next = head
        return ret_node.next
