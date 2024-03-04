import pygame
import sys
import random
from constants import *
from load_images import *
from player import *
from road import *
from enemy import *

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 36)
pygame.display.set_caption('Car Goes BOOM v2.0')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font("img/PixelifySans.ttf", 36)


def move_road():
    global ROAD_SPEED, ACCELERATION
    ROAD_SPEED += ACCELERATION

    if road1.rect.right <= 0:
        road1.rect.x = 0
        road2.rect.x = road1.rect.width
    elif road2.rect.right <= 0:
        road2.rect.x = 0
        road1.rect.x = road2.rect.width

    road1.rect.x -= ROAD_SPEED
    road2.rect.x -= ROAD_SPEED


def spawn_enemies():
    if len(enemies_group.sprites()) < 5:
        position = (random.randint(1500, 3500), random.randint(40, 560))
        enemy = Enemy(position, random.choice(enemy_images), ENEMY_SPEED)
        enemies_group.add(enemy)


def count_score():
    global POINTS
    for car in enemies_group:
        if car.rect.right < player.rect.left and not car.passed:
            POINTS += 1
            car.passed = True


def draw_all():
    screen.blit(road1.image, road1.rect)
    screen.blit(road2.image, road2.rect)
    move_road()

    global ENEMY_SPEED, PLAYER_SPEED
    ENEMY_SPEED = ENEMY_SPEED + ACCELERATION
    enemies_group.update()
    enemies_group.draw(screen)

    PLAYER_SPEED = PLAYER_SPEED + ACCELERATION
    player.draw(screen)

    timer_text = font.render("Score: " + str(POINTS), True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))


START_SCREEN = 0
RUNNING = 1
PAUSED = 2
GAME_OVER = 3

game_state = START_SCREEN
player_position = (150, 300)
POINTS = 0

ENEMY_SPEED = 8
PLAYER_SPEED = 9
ROAD_SPEED = 5


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_state == RUNNING:
                    game_state = PAUSED
                elif game_state == PAUSED or game_state == GAME_OVER:
                    game_state = RUNNING

            if event.key == pygame.K_RETURN:
                if game_state == PAUSED or game_state == GAME_OVER:
                    game_state = START_SCREEN

            if event.key == pygame.K_1:
                if game_state == START_SCREEN:
                    track_image = road_image
                    player_image = car_player_image
                    enemy_images = car_enemy_images
                    game_state = RUNNING

            if event.key == pygame.K_2:
                if game_state == START_SCREEN:
                    track_image = space_image
                    player_image = ufo_player_image
                    enemy_images = meteor_enemy_images

                    game_state = RUNNING

    if game_state == START_SCREEN:
        screen.blit(start_image, (0, 0))
        player_position = (150, 300)
        ROAD_SPEED = 5
        PLAYER_SPEED = 9
        ENEMY_SPEED = 8
        POINTS = 0
        enemies_group = pygame.sprite.Group()

    elif game_state == RUNNING:
        clock = pygame.time.Clock()
        road1 = Road(track_image, ((WIDTH * (WIDTH / 500)) / 2, HEIGHT / 2))
        road2 = Road(track_image, ((WIDTH * (WIDTH / 500)) /
                     2 + road1.rect.width, HEIGHT / 2))
        player = Player(player_position, player_image, PLAYER_SPEED)

        while game_state == RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_state = GAME_OVER

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = PAUSED
                        player_position = player.rect.topleft

            screen.fill((0, 0, 0))

            if player.status == 'alive':
                draw_all()
                spawn_enemies()
                player.move()
                player.crash_check(enemies_group)
                count_score()

            elif player.status == 'dead':
                game_state = GAME_OVER

            pygame.display.flip()
            clock.tick(60)

    elif game_state == PAUSED:
        screen.blit(pause_image, (0, 0))
        player_position = player.rect.center

    elif game_state == GAME_OVER:
        screen.blit(gameover_image, (0, 0))

        player_position = (150, 300)
        ROAD_SPEED = 5
        PLAYER_SPEED = 9
        ENEMY_SPEED = 8
        POINTS = 0
        enemies_group = pygame.sprite.Group()

    pygame.display.flip()


pygame.quit()
sys.exit()
