import pygame
import random
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

# основные настройки
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, random.randrange(400, 500))

# экран
# state = 'game'
# цикл игры
game = Game(screen, ADD_ENEMY)
while True:  # если цикл игры
    clock.tick(FPS)  # fps
    screen.fill((0, 70, 95))  # экран для меню
    game.update()  # игра
    pygame.display.flip()
