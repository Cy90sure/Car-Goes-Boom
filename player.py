import pygame
from constants import HEIGHT, WIDTH, ACCELERATION


class Player:
    def __init__(self, position, image, speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = speed
        self.status = 'alive'

    def border(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def move(self):
        self.speed += ACCELERATION
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        elif key[pygame.K_d]:
            self.rect.x += self.speed
        elif key[pygame.K_w]:
            self.rect.y -= self.speed
        elif key[pygame.K_s]:
            self.rect.y += self.speed
        self.border()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def crash_check(self, enemies_group):
        for car in enemies_group:
            if car.rect.colliderect(self.rect):
                self.status = 'dead'
