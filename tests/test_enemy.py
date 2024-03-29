import pygame
import os
import sys
from constants import ACCELERATION
from enemy import Enemy


sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
image = pygame.Surface((50, 50))
pygame.init()


def test_enemy_creation():
    enemy = Enemy((1000, 300), image, 5)
    assert enemy.image == image
    assert enemy.rect.center == (1000, 300)
    assert enemy.speed == 5
    assert not enemy.passed


def test_remove():
    enemy = Enemy((-300, 300), image, 5)
    enemy.remove()
    assert not pygame.sprite.spritecollide(enemy,
                                           pygame.sprite.Group(), dokill=False)


def test_update():
    enemy = Enemy((1000, 300), image, 5)
    speed = enemy.speed + ACCELERATION
    x = enemy.rect.x - enemy.speed
    enemy.update()
    assert enemy.speed == speed
    assert enemy.rect.x == x
