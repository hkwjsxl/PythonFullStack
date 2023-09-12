"""
小A参加了一个n人的活动，每个人都有一个唯一编号i(i>=0 & i<n)，
其中m对相互认识，在活动中两个人可以通过互相都认识的一个人介绍认识。
现在问活动结束后，小A最多会认识多少人？

时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 32M，其他语言64M
输入描述：
    第一行聚会的人数：n（n>=3 & n<10000）；
    第二行小A的编号: ai（ai >= 0 & ai < n)；
    第三互相认识的数目: m（m>=1 & m
    < n(n-1)/2）；
    第4到m+3行为互相认识的对，以','分割的编号。
输出描述：
    输出小A最多会新认识的多少人？
示例1
输入例子：
7
5
6
1,0
3,1
4,1
5,3
6,1
6,5
输出例子：
3
"""

"""
并查集算法，先把n个人视为独立的个体，依次输入人物关系时进行连接，认识的人共用一个数字，即分组；
最后根据小A编号查找他那一组一共有多少人，用这个数减去曾经就认识的人，就是答案。
"""

# n, a, m = 7, 5, 6
n, a, m = map(int, (input(), input(), input()))

from collections import defaultdict

tmp_dict = defaultdict(list)
for i in range(m):
    start, end = map(int, input().split(','))
    tmp_dict[start].append(end)
    tmp_dict[end].append(start)

# {1: [0, 3, 4, 6], 0: [1], 3: [1, 5], 4: [1], 5: [3, 6], 6: [1, 5]}
# print(tmp_dict)

visited = [False] * n
visited[a] = True
friend = set()


def recur(i):
    if (i != a) and (i not in tmp_dict[a]):
        # 注意不要把小A和小A初始已经认识的朋友加入集合中
        friend.add(i)
    # 表示 没有和当前人i认识的
    if not tmp_dict[i]:
        return
    for j in tmp_dict[i]:
        if not visited[j]:
            visited[j] = True
            recur(j)
            # visited[j] = False
            # 注意这里在递归回来时不用恢复visited，因为在这里只需要考虑深度遍历到的有哪些节点
            # 而是不是新朋友，交给递归函数里的第一个if判断就可以了
            # 加了这句反而会使有些节点被重复得递归到


recur(a)
print(len(friend))
