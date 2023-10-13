# 输入一个长度为 n 的链表，设链表中的元素的值为 ai ，返回该链表中倒数第k个节点。 如果该链表长度小于k，请返回一个长度为 0 的链表。 
#  
#  数据范围：，， 要求：空间复杂度 ，时间复杂度 进阶：空间复杂度 ，时间复杂度 
#  例如输入{1,2,3,4,5},2时，对应的链表结构如下图所示： 其中蓝色部分为该链表的最后2个结点，所以返回倒数第2个结点（也即结点值为4的结点）即可，
# 系统会打印后面所有的节点来比较。
#  
#  Related Topics 链表 
# 示例:
# 输入:{1,2,3,4,5},2
# 输出:{4,5}
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
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#
class BM8FindKthToTail:
    def FindKthToTail(self, pHead, k):
        """
        思路：循环放入列表中链表的值，取出题目中要求的值，再次组成新的链表返回
        """
        temp_list = []
        while pHead:
            temp_list.append(pHead.val)
            pHead = pHead.next

        if k > len(temp_list):
            return None

        temp_node = ListNode(None)
        ret_node = temp_node
        for val in temp_list[len(temp_list) - k:]:
            temp_node.next = ListNode(val)
            temp_node = temp_node.next
        return ret_node.next
