import pygame.image

from ParentObject import ParentObject
from Sound import Sound
from Explode import Explode

class Home(ParentObject):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../Image/Home/Home.png')
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.isDestroy = False

    def draw(self, window):
        window.blit(self.image, self.rect)

    def bulletCollidePlayerHome(self, home, explodeList):
        if pygame.sprite.collide_rect(self, home):
            self.isDestroy = True
            explode = Explode(home, 50)
            explodeList.append(explode)
            Sound('../Sound/buh.wav').play()
            return True
        else:
            return False
