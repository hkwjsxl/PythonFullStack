# 判断给定的链表中是否有环。如果有环则返回true，否则返回false。 
#  
#  数据范围：链表长度 ，链表中任意节点的值满足 
#  要求：空间复杂度 ，时间复杂度 
#  输入分为两部分，第一部分为链表，第二部分代表是否有环，然后将组成的head头结点传入到函数里面。-1代表无环，其它的数字代表有环，这些参数解释仅仅是为了方
# 便读者自测调试。实际在编程时读入的是链表的头节点。 
#  例如输入{3,2,0,-4},1时，对应的链表结构如下图所示： 
#  可以看出环的入口结点为从头结点开始的第1个结点（注：头结点为第0个结点），所以输出true。
#  
#  Related Topics 链表 哈希 双指针 
# 示例:
# 输入:{3,2,0,-4},1
# 输出:true
# 


# nowcoder submit region begin(Prohibit modification and deletion)
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return bool布尔型
#
class BM6hasCycle:
    def hasCycle(self, head):
        temp_list = []
        while head:
            if head in temp_list:
                return True
            temp_list.append(head)
            head = head.next
        return False
