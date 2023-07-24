"""队列解决迷宫问题"""

from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x - 1, y),  # 上
    lambda x, y: (x, y + 1),  # 右
    lambda x, y: (x + 1, y),  # 下
    lambda x, y: (x, y - 1),  # 左
]


def print_path(path_list):
    current_node = path_list[-1]  # 拿到最后一个节点(因为要从后往前循环，所以拿最后一个)
    real_path_list = []  # 最后正确的路径
    while current_node[2] != -1:  # 起点的[2]是-1，从后往前以此循环
        real_path_list.append(current_node[0:2])  # 前两个是路径，所以是[0:2]也就是0,1
        current_node = path_list[current_node[2]]  # 重新赋值 要判断的条件
    real_path_list.append(current_node[0:2])  # 把开始的起点放进去
    real_path_list.reverse()  # 因为是从后往前循环，所以是逆序的，要翻转回来
    for path in real_path_list:  # 循环输入
        print(path)


def maze_path(x1, y1, x2, y2):
    q = deque()  # 创建队列
    q.append((x1, y1, -1))  # 将起点入列（第三个参数表示该节点是由哪个节点走过来的，起点没有前一个节点就用-1表示）
    path_list = []  # 保存走过的路径
    while len(q) > 0:  # 队列长度为0表示无路可走了
        current_node = q.popleft()  # 当前的节点
        path_list.append(current_node)  # 将当前节点加入到保存路径的列表中
        # 判断是否到终点了
        if current_node[0] == x2 and current_node[1] == y2:
            print_path(path_list)  # 打印路径
            return True
        # 循环遍历查找下一个节点
        for d in dirs:
            next_node = d(current_node[0], current_node[1])  # 找到下一个可走的节点
            if maze[next_node[0]][next_node[1]] == 0:  # 节点为0表示路可以走
                q.append(  # 将在一个可走的节点入队列，第三个表示是由哪个路径走过来的(下标)
                    (next_node[0], next_node[1], len(path_list) - 1)
                )
                maze[next_node[0]][next_node[1]] = 2  # 标记节点已经走过了
    else:
        # 无路可走
        print("没有路径可以到终点.")
        return False


maze_path(1, 1, 8, 8)
