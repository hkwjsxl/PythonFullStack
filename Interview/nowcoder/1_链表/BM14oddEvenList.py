# 给定一个单链表，请设定一个函数，将链表的奇数位节点和偶数位节点分别放在一起，重排后输出。 注意是节点的编号而非节点的数值。 
#  数据范围：节点数量满足 ，节点中的值都满足 
#  要求：空间复杂度 ，时间复杂度 
#  Related Topics 链表 排序 
# 示例:
# 输入:{1,2,3,4,5,6}
# 输出:{1,3,5,2,4,6} 
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
class BM14oddEvenList:
    def oddEvenList(self, head):
        """
        思路：
            奇偶位分别放入两个列表中，最后合并为一个列表，然后组成新的链表
        """
        odd_list = []
        even_list = []
        i = 1
        while head:
            if i % 2 != 0:
                odd_list.append(head.val)
            else:
                even_list.append(head.val)
            i += 1
            head = head.next
        ret_list = odd_list + even_list

        # 重新组装链表
        temp_node = ListNode(None)
        ret_node = temp_node
        while ret_list:
            node = ListNode(ret_list.pop(0))
            temp_node.next = node
            temp_node = temp_node.next
        return ret_node.next
