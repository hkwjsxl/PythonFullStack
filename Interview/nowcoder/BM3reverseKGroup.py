# 将给出的链表中的节点每 k 个一组翻转，返回翻转后的链表
#  如果链表中的节点数不是 k 的倍数，将最后剩下的节点保持原样
#  你不能更改节点中的值，只能更改节点本身。 
#  数据范围： ， ，链表中每个元素都满足 
#  要求空间复杂度 ，时间复杂度 例如： 给定的链表是 对于 , 你应该返回 对于 , 你应该返回 
#  
#  Related Topics 链表 
# 示例:
# 输入:{1,2,3,4,5},2
# 输出:{2,1,4,3,5}
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
# @param k int整型 
# @return ListNode类
#
class BM3reverseKGroup:
    def reverseKGroup(self, head, k):
        """
        思路：
        链表节点放入列表中；
        mn表示每组的开始和结束，替换后两个值向中心靠近，直到替换完成；
        current_m和current_n记录当前组的位置，方便计算下一组的开始和结束位置。
        right_length是看替换完该组后 够不够再替换下一组；
        """
        if k == 1:
            return head
        temp_list = [head]
        if not temp_list[-1]:
            return head
        while temp_list[-1].next:
            temp_list.append(temp_list[-1].next)

        right_length = len(temp_list)
        m = 0
        n = k - 1
        current_m = m
        current_n = n
        while k <= right_length:
            while m < n:
                temp_list[m].val, temp_list[n].val = temp_list[n].val, temp_list[m].val
                m += 1
                n -= 1
            m = current_m + k
            n = current_n + k
            current_m, current_n = m, n
            right_length -= k
        return head
