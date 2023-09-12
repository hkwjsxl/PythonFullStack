"""
队列
时间限制： 3000MS
内存限制： 589824KB

题目描述：
给定一个长度为n的序列a1,a2,…,an，你可以选择删去其中最多n-1个数，得到一个新序列b1,b2,...,bm(1≤m≤n)。
（只是删去后的序列，不改变原来的相对顺序）

现在你希望删去某些数使得新序列的第i个数的值恰好为i，即 bi=i。
现在你想知道最少需要删去多少个数使得新序列满足条件。
如果无论如何都不能做到，请输出-1。

输入描述
    第一行一个正整数n，表示序列长度。
    接下来一行n个空格隔开的数字 a1,a2,...,an。

输出描述
    输出一个整数表示最少需要删去的个数，如果做不到，输出 -1.


样例输入
5
1 4 2 3 5

样例输出
2

提示
输入样例2
3
3 3 2
输出样例2
-1

输入样例3
5
1 2 3 4 5

输出样例3
0

样例解释
    对于第一个样例，删去第二个数字4和第五个数字5，剩下1,2,3即可满足条件。
    对于第二个样例，无论如何都做不到，输出-1。
    对于第三个样例，显然不需要删去任何数，输出0。

数据范围和说明
1≤n≤100000,1≤ai≤n
"""

"""未使用队列：通过率55%"""
# # n = eval(input(""))
# # s = input("")
# n = eval("5")
# s = "1 2 3 4 5"
# lst = s.strip().split()
# lst = list(map(int,lst))
# max_value = max(lst)
# if max_value < n:
#     print("-1")
# tmp_list = []
# m = 1
# y=0
# for i in range(n):
#     val = lst[i]
#     if val == m:
#         tmp_list.append(val)
#         m+=1
#     else:
#         y +=1
#
# # print(tmp_list)
# print(y)


"""队列：未检测通过率"""
from queue import Queue

q = Queue()

n = eval("5")
s = "1 4 2 3 5"

# n = eval("3")
# s = "3 3 2"

# n = eval("5")
# s = "1 2 3 4 5"
lst = list(map(int, s.strip().split()))
for val in lst:
    q.put(val)
q_num = 1
ret_num = 0
tmp_list = []
while not q.empty():
    q_val = q.get()
    if q_val == q_num:
        q_num += 1
        if not tmp_list:
            tmp_list.append(q_val)
    else:
        ret_num += 1
if not tmp_list:
    print("-1")
else:
    print(ret_num)
