import pygame.sprite
from constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, image, speed):
        super().__init__()
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.passed = False

    def remove(self):
        if self.rect.left < -230:
            self.kill()

    def update(self):
        self.speed += ACCELERATION
        self.rect.x -= self.speed
        self.remove()
