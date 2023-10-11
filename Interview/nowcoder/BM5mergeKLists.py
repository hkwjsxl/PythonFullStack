# 合并 k 个升序的链表并将结果作为一个升序的链表返回其头节点。 
#  数据范围：节点总数 ，每个节点的val满足 要求：时间复杂度 
#  Related Topics 堆 链表 分治 
# 示例:
# 输入:[{1,2,3},{4,5,6,7}]
# 输出:{1,2,3,4,5,6,7}
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
# @param lists ListNode类一维数组 
# @return ListNode类
#
class BM5mergeKLists:
    def mergeKLists(self, lists):
        """
        思路：循环列表，分别将链表的值加入新列表中，排序，最后重新生成链表
        """

        def get_list(node):
            temp_list = []
            while node:
                temp_list.append(node.val)
                node = node.next
            return temp_list

        ret_list = []
        for node in lists:
            ret_list += get_list(node)
        current_node = ListNode(None)
        ret_node = current_node
        for val in sorted(ret_list):
            current_node.next = ListNode(val)
            current_node = current_node.next
        return ret_node.next
