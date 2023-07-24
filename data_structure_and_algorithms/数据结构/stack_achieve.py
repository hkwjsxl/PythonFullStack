"""栈"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        # 　压栈
        self.stack.append(value)

    def pop(self):
        # 出栈
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("stack is empty.")

    def get_top(self):
        # 取栈顶
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("stack is empty.")

    def is_empty(self):
        # 是否为空栈
        return len(self.stack) == 0


def bracket_match(s):
    """
    括号匹配问题解决
    :param s:
    :return:
    """
    stack = Stack()
    bracket_dict = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    for val in s:
        if val in "([{":
            # 左括号 进栈
            stack.push(val)
        else:
            # 右括号进行匹配
            if stack.is_empty():
                # 栈为空
                return False
            elif stack.get_top() == bracket_dict[val]:
                # 括号匹配
                stack.pop()
            else:
                # 括号不匹配
                return False
    return stack.is_empty()


print(bracket_match("(){}{{}}[]"))
print(bracket_match("{(}"))
