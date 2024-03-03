import pygame
import pygame.freetype

from constants import WIDTH, HEIGHT

start_image = pygame.image.load('img/mainScreen.png')
start_image = pygame.transform.scale(start_image, (WIDTH, HEIGHT))

pause_image = pygame.image.load('img/pause.png')
pause_image = pygame.transform.scale(pause_image, (WIDTH, HEIGHT))

gameover_image = pygame.image.load('img/gameover.png')
gameover_image = pygame.transform.scale(gameover_image, (WIDTH, HEIGHT))

road_image = pygame.image.load('img/road.png')
road_image = pygame.transform.scale(road_image, (WIDTH * (WIDTH/500), HEIGHT))


car_player_image = pygame.image.load('img/playerCarBLUE.png')
car_player_image = pygame.transform.scale(car_player_image, (220, 80))

car_enemy_image1 = pygame.image.load('img/enemyCar1.png')
car_enemy_image1 = pygame.transform.scale(car_enemy_image1, (230, 90))
car_enemy_image2 = pygame.image.load('img/enemyCar2.png')
car_enemy_image2 = pygame.transform.scale(car_enemy_image2, (230, 90))
car_enemy_image3 = pygame.image.load('img/enemyCar3.png')
car_enemy_image3 = pygame.transform.scale(car_enemy_image3, (230, 90))
car_enemy_image4 = pygame.image.load('img/enemyCar4.png')
car_enemy_image4 = pygame.transform.scale(car_enemy_image4, (230, 90))
car_enemy_image5 = pygame.image.load('img/enemyCar5.png')
car_enemy_image5 = pygame.transform.scale(car_enemy_image5, (230, 90))
car_enemy_images = [car_enemy_image1, car_enemy_image2, car_enemy_image3, car_enemy_image4, car_enemy_image5]


space_image = pygame.image.load('img/cosmos.png')
space_image = pygame.transform.scale(space_image, (WIDTH * (WIDTH/500), HEIGHT))

ufo_player_image = pygame.image.load('img/playerUFO.png')
ufo_player_image = pygame.transform.scale(ufo_player_image, (220, 80))

meteor_enemy_image1 = pygame.image.load('img/meteor1.png')
meteor_enemy_image1 = pygame.transform.scale(meteor_enemy_image1, (90, 90))
meteor_enemy_image2 = pygame.image.load('img/meteor2.png')
meteor_enemy_image2 = pygame.transform.scale(meteor_enemy_image2, (90, 90))
meteor_enemy_image3 = pygame.image.load('img/meteor3.png')
meteor_enemy_image3 = pygame.transform.scale(meteor_enemy_image3, (90, 90))
meteor_enemy_image4 = pygame.image.load('img/meteor4.png')
meteor_enemy_image4 = pygame.transform.scale(meteor_enemy_image4, (90, 90))
meteor_enemy_image5 = pygame.image.load('img/meteor5.png')
meteor_enemy_image5 = pygame.transform.scale(meteor_enemy_image5, (90, 90))
meteor_enemy_images = [meteor_enemy_image1, meteor_enemy_image2, meteor_enemy_image3,
                       meteor_enemy_image4, meteor_enemy_image5]