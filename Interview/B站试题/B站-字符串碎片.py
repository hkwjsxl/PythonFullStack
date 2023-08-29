"""
字符串碎片
一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。
例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。
现在给定一个字符串,请你帮助计算这个字符串的所有碎片的平均长度是多少，结果直接取整，无需保留小数
时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 256M，其他语言512M
示例1
输入例子：
    "aaabbaaac"
输出例子：
    2
例子说明：
所有碎片的平均长度= (3 + 2 + 3 + 1) / 4 = 2
"""


class Solution:
    def GetFragment(self, str):
        if not str:
            return 0
        temp_list = [0 for _ in range(10)]
        last_str = str[0]
        i = 0
        for value in str:
            if value == last_str:
                temp_list[i] += 1
            else:
                i += 1
                last_str = value
                temp_list[i] += 1
        # print(temp_list)
        ret = 0
        for num in temp_list:
            ret += num
        return ret // (i + 1)


ret = Solution().GetFragment("aaabbaaac")
print(ret)
