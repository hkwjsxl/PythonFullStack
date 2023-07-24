"""栈解决迷宫问题"""

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


def maze_path(x1, y1, x2, y2):
    """
    :param x1: 起点x坐标
    :param y1: 起点y坐标
    :param x2: 终点x坐标
    :param y2: 终点y坐标
    :return: bool
    """
    stack = []  # 创建栈
    stack.append((x1, y1))  # 将起点位置进栈
    while len(stack) > 0:  # 栈长度为0时为空栈，即没有路径
        current_node = stack[-1]  # 当前的节点
        # 判断是否到终点了
        if current_node[0] == x2 and current_node[1] == y2:
            # 到终点就输出路径
            for path in stack:
                print(path)
            print("到终点了.")
            return True
        # 循环找下一个节点
        for d in dirs:
            next_node = d(current_node[0], current_node[1])  # 找出下一个节点
            if maze[next_node[0]][next_node[1]] == 0:  # 等于0表示该路可以走
                stack.append(next_node)  # 找到下一个节点后保存一下节点
                maze[next_node[0]][next_node[1]] = 2  # 设置成2表示这个点走过了
                break  # 找到下一个节点后退出循环
        else:
            # 没有找到下一个节点，回退
            maze[next_node[0]][next_node[1]] = 2  # 设置成2表示这个点走过了
            stack.pop()
    else:
        # 没有路径
        print("没有路径可以到终点.")
        return False


maze_path(1, 1, 8, 8)
