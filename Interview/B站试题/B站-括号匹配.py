"""
给定一个只包含括号的字符串，判断字符串是否有效。
其中，括号种类包含： ‘(’，’)’，’{’，’}’，’[’，’]'。
有效字符串需满足：
1) 左括号必须用相同类型的右括号闭合；
2）左括号必须以正确的顺序闭合。注意空字符串可被认为是有效字符串

示例1
输入例子：
"{[]}"
输出例子：
true
示例2
输入例子：
"([)]"
输出例子：
false
示例3
输入例子：
"([]"
输出例子：
false
"""


#
#
# @param s string字符串
# @return bool布尔型
#
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def get_top(self):
        if self.is_empty():
            return None
        return self.stack[-1]


class Solution:
    def IsValidExp(self, s):
        if len(s) % 2 != 0:
            return False
        stack = Stack()
        stack_dict = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for value in s:
            if value in "([{":
                stack.push(value)
            else:
                if stack.is_empty():
                    return False
                elif stack.get_top() == stack_dict[value]:
                    stack.pop()
                else:
                    return False
        return stack.is_empty()


Solution().IsValidExp("{[]}")
Solution().IsValidExp("([)]")
Solution().IsValidExp("([]")
