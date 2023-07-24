"""建造者模式"""

from abc import ABCMeta, abstractmethod


class Player:
    """基础人物模型"""

    def __init__(self, name=None, face=None, body=None, blood=None):
        self.name = name
        self.face = face
        self.body = body
        self.blood = blood

    def __str__(self):
        return "%s-%s-%s-%s" % (self.name, self.face, self.body, self.blood)


class PlayerBuilder(metaclass=ABCMeta):
    """基础人物构建模型"""

    @abstractmethod
    def build_name(self):
        pass

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_blood(self):
        pass


class People(PlayerBuilder):
    """人类玩家"""

    def __init__(self):
        self.player = Player()

    def build_name(self):
        self.player.name = "普通人"

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "健壮的身体"

    def build_blood(self):
        self.player.blood = "100"


class Monster(PlayerBuilder):
    """野兽玩家"""

    def __init__(self):
        self.player = Player()

    def build_name(self):
        self.player.name = "野兽"

    def build_face(self):
        self.player.face = "狰狞恐怖"

    def build_body(self):
        self.player.body = "骨骼奇特"

    def build_blood(self):
        self.player.blood = "1000"


if __name__ == '__main__':
    # client

    class Build:
        def start_build(self, build):
            build.build_name()
            build.build_face()
            build.build_body()
            build.build_blood()
            return build.player


    bulid = Build()
    player_info = bulid.start_build(Monster())
    print(player_info)
