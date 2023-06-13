import pygame


class Sound:
    def __init__(self, filename):
        self.filename = filename
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(self.filename)

    def play(self, loops=0):
        self.sound.play(loops)

    def stop(self):
        self.sound.stop()

    def setVolume(self):
        self.sound.set_volume(0.2)
        return self
