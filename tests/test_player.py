from enemy import Enemy
from constants import HEIGHT, WIDTH
from player import Player
import pygame
import pytest
import os
import sys
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))
image = pygame.Surface((50, 50))

pygame.init()


def test_player_creation():
    position = (100, 200)
    speed = 5

    player = Player(position, image, speed)
    assert player.image == image
    assert player.rect.center == position
    assert player.speed == speed
    assert player.status == 'alive'


@pytest.fixture
def player():
    return Player((300, 300), image, 5)


def test_borders(player):
    player.border()
    assert player.rect.top >= 0
    assert player.rect.bottom <= HEIGHT
    assert player.rect.right <= WIDTH
    assert player.rect.left >= 0

    player = Player((10000, 10000), image, 5)
    player.border()
    assert player.rect.top >= 0
    assert player.rect.bottom <= HEIGHT
    assert player.rect.right <= WIDTH
    assert player.rect.left >= 0

    player = Player((-1000, -1000), image, 5)
    player.border()
    assert player.rect.top >= 0
    assert player.rect.bottom <= HEIGHT
    assert player.rect.right <= WIDTH
    assert player.rect.left >= 0


def test_crash():
    player = Player((300, 300), image, 5)
    assert player.status == 'alive'

    enemies_group = pygame.sprite.Group()

    enemy = Enemy((500, 500), image, 5)
    enemies_group.add(enemy)
    player.crash_check(enemies_group)
    assert player.status == 'alive'

    enemy = Enemy((330, 300), image, 5)
    enemies_group.add(enemy)
    player.crash_check(enemies_group)
    assert player.status == 'dead'
