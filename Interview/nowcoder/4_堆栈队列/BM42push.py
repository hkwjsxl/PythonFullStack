# 用两个栈来实现一个队列，使用n个元素来完成 n 次在队列尾部插入整数(push)和n次在队列头部删除整数(pop)的功能。 队列中的元素为int类型。保证操
# 作合法，即保证pop操作时队列内已有元素。 
#  数据范围： 要求：存储n个元素的空间复杂度为 ，插入与删除的时间复杂度都是 
#  Related Topics 栈 
# 示例:
# 输入:["PSH1","PSH2","POP","POP"]
# 输出:1,2
# 

# -*- coding:utf-8 -*-
class BM42push:
    """两个栈实现队列"""

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
