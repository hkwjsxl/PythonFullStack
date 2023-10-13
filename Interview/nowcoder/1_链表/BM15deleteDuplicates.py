# 删除给出链表中的重复元素（链表中元素从小到大有序），使链表中的所有元素都只出现一次
#  例如：
#  给出的链表为,返回.
#  给出的链表为,返回. 
#  数据范围：链表长度满足 ，链表中任意节点的值满足 进阶：空间复杂度 ，时间复杂度 
#  
#  Related Topics 链表 
# 示例:
# 输入:{1,1,2}
# 输出:{1,2}
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
class BM15deleteDuplicates:
    def deleteDuplicates(self, head):
        """
        思路：
            将链表中的值都存入集合中，去重后转换为列表，排序后重新生成新链表
        """
        if not head:
            return head
        temp_set = set()
        while head:
            temp_set.add(head.val)
            head = head.next
        temp_list = list(temp_set)
        temp_list.sort()

        temp_node = ListNode(None)
        ret_node = temp_node
        for val in temp_list:
            temp_node.next = ListNode(val)
            temp_node = temp_node.next
        return ret_node.next
