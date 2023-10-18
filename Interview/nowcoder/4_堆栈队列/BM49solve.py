# 请写一个整数计算器，支持加减乘三种运算和括号。 
#  数据范围：，保证计算结果始终在整型范围内 
#  要求：空间复杂度： ，时间复杂度 
#  Related Topics 栈 递归 
# 示例:
# 输入:"1+2"
# 输出:3 
# 


# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
class BM49solve:
    def solve(self, s):
        return eval(s)
