# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数，输入操作时保证 pop、top 和 min 函数操作时，栈中一定有元素。 
#  此栈包含的方法有： push(value):将value压入栈中 pop():弹出栈顶元素 top():获取栈顶元素 min():获取栈中最小元素 
#  数据范围：操作数量满足 ，输入的元素满足 
#  进阶：栈的各个操作的时间复杂度是 ，空间复杂度是 
#  
#  示例: 输入: ["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"] 输出: -1,2,1,-1 解
# 析: "PSH-1"表示将-1压入栈中，栈中元素为-1 "PSH2"表示将2压入栈中，栈中元素为2，-1 “MIN”表示获取此时栈中最小元素==>返回-1 
# "TOP"表示获取栈顶元素==>返回2 "POP"表示弹出栈顶元素，弹出2，栈中元素为-1 "PSH1"表示将1压入栈中，栈中元素为1，-1
#  "TOP"表示获取栈顶元素==>返回1 “MIN”表示获取此时栈中最小元素==>返回-1
#  
#  
#  Related Topics 栈 
# 示例:
# 输入: ["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"]
# 输出:-1,2,1,-1
# 


# -*- coding:utf-8 -*-
class BM43push:
    """栈的操作"""

    def __init__(self):
        self.temp_list = []

    def push(self, node):
        self.temp_list.append(node)

    def pop(self):
        self.temp_list.pop()

    def top(self):
        return self.temp_list[-1]

    def min(self):
        return min(self.temp_list)
