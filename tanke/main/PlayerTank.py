import pygame
import pygame.image
from ParentObject import ParentObject
from Bullet import Bullet


class PlayerTank(ParentObject):
    def __init__(self, x, y, order, amour):
        """

        :param x: 坦克横坐标
        :param y: 坦克纵坐标
        :param order: 玩家坦克序号，1表示一号玩家，2表示二号玩家
        :param amour: 坦克初始护甲
        """
        super().__init__()
        self.images = []
        if order == 1:
            self.images.append({
                'UP': pygame.image.load('../Image/Player1/45x45/UP1.png'),
                'DOWN': pygame.image.load('../Image/Player1/45x45/DOWN1.png'),
                'LEFT': pygame.image.load('../Image/Player1/45x45/LEFT1.png'),
                'RIGHT': pygame.image.load('../Image/Player1/45x45/RIGHT1.png')
            })
            self.images.append({
                'UP': pygame.image.load('../Image/Player1/45x45/UP2.png'),
                'DOWN': pygame.image.load('../Image/Player1/45x45/DOWN2.png'),
                'LEFT': pygame.image.load('../Image/Player1/45x45/LEFT2.png'),
                'RIGHT': pygame.image.load('../Image/Player1/45x45/RIGHT2.png')
            })
            self.images.append({
                'UP': pygame.image.load('../Image/Player1/45x45/UP3.png'),
                'DOWN': pygame.image.load('../Image/Player1/45x45/DOWN3.png'),
                'LEFT': pygame.image.load('../Image/Player1/45x45/LEFT3.png'),
                'RIGHT': pygame.image.load('../Image/Player1/45x45/RIGHT3.png')
            })
            self.images.append({
                'UP': pygame.image.load('../Image/Player1/45x45/UP4.png'),
                'DOWN': pygame.image.load('../Image/Player1/45x45/DOWN4.png'),
                'LEFT': pygame.image.load('../Image/Player1/45x45/LEFT4.png'),
                'RIGHT': pygame.image.load('../Image/Player1/45x45/RIGHT4.png')
            })
            self.images.append({
                'UP': pygame.image.load('../Image/Player1/45x45/UP5.png'),
                'DOWN': pygame.image.load('../Image/Player1/45x45/DOWN5.png'),
                'LEFT': pygame.image.load('../Image/Player1/45x45/LEFT5.png'),
                'RIGHT': pygame.image.load('../Image/Player1/45x45/RIGHT5.png')
            })
            self.images.append({
                'UP': pygame.image.load('../Image/Player1/45x45/UP6.png'),
                'DOWN': pygame.image.load('../Image/Player1/45x45/DOWN6.png'),
                'LEFT': pygame.image.load('../Image/Player1/45x45/LEFT6.png'),
                'RIGHT': pygame.image.load('../Image/Player1/45x45/RIGHT6.png')
            })

        # 生命
        self.life = 3
        # 装甲
        self.armor = amour

        # 方向
        self.direction = 'UP'

        # 根据护甲选择坦克的样子
        self.image: pygame.Surface = self.images[max(self.armor - 1, 0)][self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

        # 速度
        self.accumulation: float = 0
        self.speed = 2
        # 移动开关
        self.stop = True
        # 重生
        self.isResurrecting = False
        # 碰撞前的坐标
        self.prvX = self.rect.left
        self.prvY = self.rect.top

        # 等级
        self.level = 1
        # 伤害
        self.damage = 1

    def move(self):
        if self.accumulation >= 1:
            self.accumulation = 0
            # 记录上一次的位置
            self.prvX = self.rect.left
            self.prvY = self.rect.top
            if self.direction == 'LEFT':
                if self.rect.left > 0:
                    self.rect.left -= self.speed
            elif self.direction == 'UP':
                if self.rect.top > 0:
                    self.rect.top -= self.speed
            elif self.direction == 'DOWN':
                if self.rect.top < 555:
                    self.rect.top += self.speed
            elif self.direction == 'RIGHT':
                if self.rect.left < 855:
                    self.rect.left += self.speed
        else:
            self.accumulation += 0.20

    def shot(self):
        return Bullet(self)

    def draw(self, window, x, y):
        # 坦克生命中为0，表示已经死亡，不再展示坦克
        if self.life <= 0:
            return
        # 判断坦克是否复合
        if self.isResurrecting:
            # 把坦克位置设置为指定的重生位置
            self.rect.left = x
            self.rect.top = y
            self.isResurrecting = False
            self.direction = 'UP'
        # 获取展示的对象
        self.image = self.images[max(self.armor - 1, 0)][self.direction]
        # 画出图片
        window.blit(self.image, self.rect)

    def collideEnemyTank(self, enemyTankList):
        # 遍历全部敌方坦克，检查有没有碰撞
        for enemyTank in enemyTankList:
            if pygame.sprite.collide_rect(self, enemyTank):
                # 如果碰撞了，就保持原来的位置
                self.rect.left = self.prvX
                self.rect.top = self.prvY

    def loseLife(self, value=1):
        self.life -= value

    def collideBrickWall(self, brickWallList):
        for brickWall in brickWallList:
            if pygame.sprite.collide_rect(self, brickWall):
                self.rect.left = self.prvX
                self.rect.top = self.prvY

    def collideStoneWall(self, stoneWallList):
        for stoneWall in stoneWallList:
            if pygame.sprite.collide_rect(self, stoneWall):
                self.rect.left = self.prvX
                self.rect.top = self.prvY

    def collideHome(self, home):
        if pygame.sprite.collide_rect(self, home):
            self.rect.left = self.prvX
            self.rect.top = self.prvY
