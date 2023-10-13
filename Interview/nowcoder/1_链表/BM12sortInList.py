# 给定一个节点数为n的无序单链表，对其按升序排序。 数据范围：，保证节点权值在之内。 要求：空间复杂度 ，时间复杂度 
#  Related Topics 链表 排序 
# 示例:
# 输入:[1,3,2,4,5]
# 输出:{1,2,3,4,5}
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
# @param head ListNode类 the head node
# @return ListNode类
#
class BM12sortInList:
    def sortInList(self, head):
        """
        思路：
            将链表中的各值放入列表中，排序后，重新生成新的链表；
        """
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
        temp_list = sorted(temp_list)

        temp_node = ListNode(None)
        ret_node = temp_node
        for val in temp_list:
            temp_node.next = ListNode(val)
            temp_node = temp_node.next
        return ret_node.next
