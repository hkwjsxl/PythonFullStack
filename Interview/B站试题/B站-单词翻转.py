"""
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
示例 1：
输入: "the sky is blue"
输出: "blue is sky the"
示例 2：
输入: "  hello world!  "
输出: "world! hello"
"""


class Solution:
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])  # 将分离后的列表进行反转，然后再拼接


ret = Solution().reverseWords("the sky is blue")
print(ret)
