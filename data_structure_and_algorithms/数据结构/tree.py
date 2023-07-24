"""树的简单示例---模拟文件管理目录结构"""


class Node:
    def __init__(self, name, type="dir"):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # 必须以"/"结尾
        if name[-1] != "/":
            name += "/"
        new_node = Node(name)
        self.now.children.append(new_node)
        new_node.parent = self.now

    def ls(self):
        print(self.now.children)

    def cd(self, name):
        # 必须以"/"结尾
        if name[-1] != "/":
            name += "/"
        # cd到上一层
        if name == "../":
            self.now = self.now.parent
            return
        # 以相对路径cd
        for child in self.now.children:
            if child.name == name and child.type == "dir":
                self.now = child
                return
        raise ValueError("invalid value.")


tree = FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
tree.ls()

tree.cd("bin/")
tree.mkdir("python/")
tree.ls()

tree.cd("../")
tree.ls()
