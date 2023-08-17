class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


node = Node(1, Node(2, None, None), Node(3, None, None))


def return_result(node):
    total = 0
    if node is not None:
        total += node.data
        total += return_result(node.left)
        total += return_result(node.right)
    return total


print(return_result(node))
