import random
import pygame
import pygame.image

from ParentObject import ParentObject
from Bullet import Bullet


class EnemyTank(ParentObject):
    def __init__(self, x, y):
        super().__init__()
        types = [(1, 3), (2, 1), (3, 2), (4, 10)]
        # 随机产生一种坦克
        self.type = types[random.randint(0, len(types) - 1)]
        up = []
        down = []
        left = []
        right = []
        for i in range(1, self.type[1] + 1):
            up.append(
                pygame.image.load(
                    '../Image/Enemy/EnemyTank' + str(self.type[0]) + '/EnemyTank' + str(self.type[0]) + 'Lv' + str(
                        i) + '(UP).png'
                )
            )
            down.append(
                pygame.image.load(
                    '../Image/Enemy/EnemyTank' + str(self.type[0]) + '/EnemyTank' + str(self.type[0]) + 'Lv' + str(
                        i) + '(DOWN).png'
                )
            )
            left.append(
                pygame.image.load(
                    '../Image/Enemy/EnemyTank' + str(self.type[0]) + '/EnemyTank' + str(self.type[0]) + 'Lv' + str(
                        i) + '(LEFT).png'
                )
            )
            right.append(
                pygame.image.load(
                    '../Image/Enemy/EnemyTank' + str(self.type[0]) + '/EnemyTank' + str(self.type[0]) + 'Lv' + str(
                        i) + '(RIGHT).png'
                )
            )
        self.images = {
            'UP': up,
            'DOWN': down,
            'LEFT': left,
            'RIGHT': right
        }
        # 生命
        self.life = self.type[1]

        # 方向
        self.direction = 'DOWN'
        self.image: pygame.Surface = self.images[self.direction][self.life - 1]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

        # 碰撞前的坐标
        self.prvX = self.rect.left
        self.prvY = self.rect.top

        # 速度
        self.accumulationMax: float = 0
        self.accumulation = 0.1

        speed = 0
        maxBulletCount = 0
        damage = 1
        # 每种坦克都有不同的属性
        if self.type[0] == 1:
            speed = 3
            self.level = 1
            maxBulletCount = 1
        elif self.type[0] == 2:
            speed = 5
            self.level = 2
            maxBulletCount = 1
            damage = 3
        elif self.type[0] == 3:
            speed = 7
            self.level = 1
            maxBulletCount = 3
            damage = 2
        elif self.type[0] == 4:
            speed = 6
            self.level = 2
            maxBulletCount = 3
            damage = 1
        self.speed = speed
        # 移动开关
        self.stop = True
        # 开火开关
        self.fire = True
        # 步数
        self.step = 30
        # 伤害
        self.damage = damage
        # 子弹个数
        self.bulletCount = 0
        self.maxBulletCount = maxBulletCount

    def loseLife(self, value=1):
        self.life -= value

    def move(self):
        """
        新增步数变量, 当坦克移动时, 步数进行减少, 当步数小于等于0的时候, 修改地方坦克的方向
        :return: None
        """
        if self.stop:
            if self.step <= 0:
                self.direction = self.randDirection()
                self.step = 30
            else:
                if self.accumulationMax >= 1:
                    self.accumulationMax = 0
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
                    self.step -= 1
                else:
                    self.accumulationMax += self.accumulation

    def shot(self):
        if self.fire:
            if self.bulletCount < self.maxBulletCount:
                num = random.randint(0, 100)
                if num == 5 or num == 6:
                    self.bulletCount += 1
                    return Bullet(self)
        return None

    def draw(self, window):
        # 获取展示的对象
        self.image = self.images[self.direction][self.life - 1]
        window.blit(self.image, self.rect)

    def randDirection(self):
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index = random.randint(0, 3)
        return directions[index]

    def collidePlayerTank(self, playerTank):
        # 遍历全部敌方坦克，检查有没有碰撞
        if pygame.sprite.collide_rect(self, playerTank):
            # 如果碰撞了，就保持原来的位置
            self.rect.left = self.prvX
            self.rect.top = self.prvY

    def collideEnemyTank(self, enemyTankList):
        for tank in enemyTankList:
            if pygame.sprite.collide_rect(self, tank) and tank != self:
                self.rect.left = self.prvX
                self.rect.top = self.prvY

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
