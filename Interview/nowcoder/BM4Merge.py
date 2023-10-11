# 输入两个递增的链表，单个链表的长度为n，合并这两个链表并使新链表中的节点仍然是递增排序的。
#  数据范围： ，
#  要求：空间复杂度 ，时间复杂度 
#  
#  如输入{1,3,5},{2,4,6}时，合并后的链表为{1,2,3,4,5,6}，所以对应的输出为{1,2,3,4,5,6}，转换过程如下图所示： 
#  
#  或输入{-1,2,4},{1,3,4}时，合并后的链表为{-1,1,2,3,4,4}，所以对应的输出为{-1,1,2,3,4,4}，转换过程如下图所示： 
# 
#  
#  Related Topics 链表 2021 
# 示例:
# 输入:{1,3,5},{2,4,6}
# 输出:{1,2,3,4,5,6}
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
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class BM4Merge:
    def Merge(self, pHead1, pHead2):
        """
        思路：将链表值都加入到列表中，排序后，再生成链表
        """
        def get_list(node):
            temp_list = []
            while node:
                temp_list.append(node.val)
                node = node.next
            return temp_list

        if not all([pHead1, pHead2]):
            return pHead1 or pHead2
        lst1 = get_list(pHead1)
        lst2 = get_list(pHead2)
        ret_list = sorted(lst1 + lst2)
        current_node = ListNode(None)
        ret_node = current_node
        for val in ret_list:
            current_node.next = ListNode(val)
            current_node = current_node.next
        return ret_node.next
