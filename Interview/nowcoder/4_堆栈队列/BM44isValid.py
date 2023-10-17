# 给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
#  括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
#  
#  数据范围：字符串长度 要求：空间复杂度 ，时间复杂度 
#  Related Topics 栈 字符串 
# 示例:
# 输入:"["
# 输出:false 
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return bool布尔型
#
class BM44isValid:
    def isValid(self, s):
        """有效括号"""
        # # 长度为奇数一定不匹配
        # if len(s) %2 == 1:
        #     return False
        # temp_list = []
        # temp_dict = {
        #     "}": "{",
        #     "]": "[",
        #     ")": "(",
        # }
        # for val in s:
        #     if val in "{[(":
        #         # 入栈
        #         temp_list.append(val)
        #     else:
        #         # 出栈
        #         if not temp_list:
        #             return False
        #         if temp_dict.get(val) != temp_list.pop():
        #             return False
        # if temp_list:
        #     return False
        # return True

        # 长度为奇数一定不匹配
        if len(s) % 2 == 1:
            return False
        while "{}" in s or "[]" in s or "()" in s:
            s = s.replace("{}", "").replace("[]", "").replace("()", "")
        if s:
            return False
        return True
