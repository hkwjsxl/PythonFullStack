import pygame
from ParentObject import ParentObject
from Explode import Explode
from Sound import Sound


class Bullet(ParentObject):
    def __init__(self, tank):
        super().__init__()
        self.images = {
            'UP': pygame.image.load('../Image/Bullet/Bullet(UP).png'),
            'DOWN': pygame.image.load('../Image/Bullet/Bullet(DOWN).png'),
            'LEFT': pygame.image.load('../Image/Bullet/Bullet(LEFT).png'),
            'RIGHT': pygame.image.load('../Image/Bullet/Bullet(RIGHT).png')
        }
        # 方向
        self.direction = tank.direction
        self.image: pygame.Surface = self.images[self.direction]
        self.rect = self.image.get_rect()

        # 坦克发射子弹的位置
        if self.direction == 'UP':
            self.rect.left = tank.rect.left + 17.5
            self.rect.top = tank.rect.top - 25
        elif self.direction == 'DOWN':
            self.rect.left = tank.rect.left + 17.5
            self.rect.top = tank.rect.top + 25
        elif self.direction == 'LEFT':
            self.rect.left = tank.rect.left - 25
            self.rect.top = tank.rect.top + 17.5
        elif self.direction == 'RIGHT':
            self.rect.left = tank.rect.left + 25
            self.rect.top = tank.rect.top + 17.5

        # 速度
        self.accumulationMax: float = 0
        self.accumulation = 0.25
        self.speed = 10
        # 销毁开关
        self.isDestroy = False
        # 发射源
        self.source = tank
        # 伤害
        self.damage = tank.damage

    def move(self, explodeList):
        if self.accumulation >= 1:
            self.accumulation = 0
            if self.direction == 'LEFT':
                self.rect.left -= self.speed
            elif self.direction == 'UP':
                self.rect.top -= self.speed
            elif self.direction == 'DOWN':
                self.rect.top += self.speed
            elif self.direction == 'RIGHT':
                self.rect.left += self.speed
            # 检查子弹是否出界
            self.checkBullet(explodeList)
        else:
            self.accumulation += 0.20

    def checkBullet(self, explodeList):
        toDestroy = False
        # 如果出界，就设置为销毁
        if self.rect.top < 0 or self.rect.top > 600:
            toDestroy = True
        if self.rect.left < 0 or self.rect.right > 900:
            toDestroy = True
        if toDestroy:
            explode = Explode(self, 25)
            explodeList.append(explode)
            self.isDestroy = True
            Sound('../Sound/block.wav').play()

    def draw(self, window):
        window.blit(self.image, self.rect)

    def playerBulletCollideEnemyTank(self, enemyTankList, explodeList):
        # 循环遍历坦克列表，检查是否发生了碰撞
        for tank in enemyTankList:
            if pygame.sprite.collide_rect(tank, self):
                tank.loseLife(self.damage)
                # 把子弹设置为销毁状态
                self.isDestroy = True
                if tank.life == 0:
                    # 增加爆炸效果
                    explode = Explode(tank, 50)
                    explodeList.append(explode)
                    Sound('../Sound/kill.wav').play()
                else:
                    Sound('../Sound/enemy.armor.hit.wav').play()

    def enemyBulletCollidePlayerTank(self, playerTank, explodeList):
        # 玩家坦克生命值为0，不用检测
        if playerTank.life <= 0:
            return
        # 检测是否发生碰撞
        if pygame.sprite.collide_rect(playerTank, self):
            # 发生碰撞先减少护甲，护甲为0时扣减生命值
            if playerTank.armor > 0:
                playerTank.armor -= self.damage
                playerTank.armor = max(0, playerTank.armor)
                Sound('../Sound/enemy.armor.hit.wav').play()
            else:
                playerTank.loseLife(self.damage)
                # 增加爆炸效果
                explode = Explode(playerTank, 50)
                explodeList.append(explode)
                playerTank.life = max(0, playerTank.life)
                Sound('../Sound/kill.wav').play()
                if playerTank.life != 0:
                    playerTank.isResurrecting = True
            # 让子弹销毁
            self.isDestroy = True

    def bulletCollideBrickWall(self, brickWallList, explodeList):
        for brickWall in brickWallList:
            # 子弹与墙发生碰撞
            if pygame.sprite.collide_rect(self, brickWall):
                self.isDestroy = True
                brickWall.isDestroy = True
                # 碰撞出现爆炸效果
                explode = Explode(brickWall, 25)
                explodeList.append(explode)
                # 出现爆炸播放音效
                Sound('../Sound/block.wav').play()

    def bulletCollideStoneWall(self, stoneWallList, explodeList):
        for stoneWall in stoneWallList:
            if pygame.sprite.collide_rect(self, stoneWall):
                # 判断坦克的等级，大于等于2时，可以打穿石墙
                if self.source.level >= 2:
                    stoneWall.isDestroy = True
                self.isDestroy = True
                explode = Explode(stoneWall, 25)
                explodeList.append(explode)
                Sound('../Sound/block.wav').play()
