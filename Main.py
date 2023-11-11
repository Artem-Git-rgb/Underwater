import pygame
import random
import time
from pygame.locals import (  # назначаю клавиши
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    K_SPACE
)
class Game():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ADD_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENEMY, 800)
    player = PLayer()
    screen.fill((0, 20, 150))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.sprite.
        self.rect = pygame.image.get_rect()
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys == K_UP:
            self.rect.move_ip(0, -5)
        if pressed_keys == K_DOWN:
            self.rect.move_ip(0, 5)
        if pressed_keys == K_LEFT:
            self.rect.move_ip(-5, 0)
        if pressed_keys == K_RIGHT:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        # если граница карты
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.vertical == 1:
            if self.rect.top < -10:
                self.rect.top = -10
        else:
            if self.rect.top < 0:
                self.rect.top = 0

        if self.vertical == -1:
            if self.rect.bottom > SCREEN_HEIGHT - 10:
                self.rect.bottom = SCREEN_HEIGHT - 10
        else:
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT