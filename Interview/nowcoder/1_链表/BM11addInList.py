# 假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。 给定两个这种链表，请生成代表两个整数相加值的结果链表。 数据范围：，链表任
# 意值 
#  要求：空间复杂度 ，时间复杂度 
#  
#  例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0。 
#  
#  Related Topics 链表 模拟 
# 示例:
# 输入:[9,3,7],[6,3]
# 输出:{1,0,0,0}
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
# @param head1 ListNode类 
# @param head2 ListNode类 
# @return ListNode类
#
class BM11addInList:
    def addInList(self, head1, head2):
        """
        思路：
            放入栈中，依次从末尾取值进行相加，记录当前进位，
            短的一方结束后，将长的一方剩余的值也加入到链表中，
            如果最后的进位大于0 也要添加到最后的结果当中
        """
        if not head1:
            return head2
        if not head2:
            return head1

        def get_list(node):
            temp_list = []
            while node:
                temp_list.append(node.val)
                node = node.next
            return temp_list

        s1 = get_list(head1)
        s2 = get_list(head2)

        temp_node = ListNode(None)
        j = 0  # 进位
        while len(s1) > 0 and len(s2) > 0:
            val_1 = s1.pop()
            val_2 = s2.pop()
            sum_val = val_1 + val_2 + j
            node = ListNode(sum_val % 10)
            node.next = temp_node.next
            temp_node.next = node
            j = sum_val // 10
        # s2先空
        while len(s1) > 0:
            val = s1.pop()
            sum_val = val + j
            node = ListNode(sum_val % 10)
            node.next = temp_node.next
            temp_node.next = node
            j = sum_val // 10
        # s1先空
        while len(s2) > 0:
            val = s2.pop()
            sum_val = val + j
            node = ListNode(sum_val % 10)
            node.next = temp_node.next
            temp_node.next = node
            j = sum_val // 10
        # 进位为0时不需要添加到头部了
        if j>0:
            node = ListNode(j)
            node.next = temp_node.next
            temp_node.next = node
        return temp_node.next
