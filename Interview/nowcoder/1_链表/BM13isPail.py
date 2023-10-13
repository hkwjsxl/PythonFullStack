# 给定一个链表，请判断该链表是否为回文结构。 回文是指该字符串正序逆序完全一致。 数据范围： 链表节点数 ，链表中每个节点的值满足 
#  Related Topics 链表 双指针 
# 示例:
# 输入:{1}
# 输出:true
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
# @param head ListNode类 the head
# @return bool布尔型
#
class BM13isPail:
    def isPail(self, head):
        """
        思路：
            放入列表中，与反转后的列表进行比较，相同则True，反之False
        """
        from copy import deepcopy
        # 只有一个节点
        if not head.next:
            return True
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next

        reverse_list = deepcopy(temp_list)
        reverse_list.reverse()

        if temp_list == reverse_list:
            return True
        return False
