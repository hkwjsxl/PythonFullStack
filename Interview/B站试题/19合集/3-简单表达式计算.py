"""
给定一个合法的表达式字符串，其中只包含非负整数、加法、减法以及乘法符号（不会有括号），
例如7+3*4*5+2+4-3-1，请写程序计算该表达式的结果并输出；

时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 32M，其他语言64M
输入描述：
输入有多行，每行是一个表达式，输入以END作为结束
输出描述：
每行表达式的计算结果
示例1
输入例子：
7+3*4*5+2+4-3-1
2-3*1
END
输出例子：
69
-1
"""

while True:
    s = input().strip()
    if s == "END":
        break
    print(eval(s))
