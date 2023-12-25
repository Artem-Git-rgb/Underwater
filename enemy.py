import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # изображение
        self.points = Game.__init__().points
        self.image = pygame.image.load("enemy_image.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (20, 30))
        self.image = pygame.transform.rotate(self.image, 180)
        # далее
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = 0
        if self.points < 10:
            self.speed = random.randint(2, 3)
        elif self.points < 20:
            self.speed = random.randint(3, 4)
        else:
            self.speed = random.randint(4, 5)

    def update(self):
        # движение врага
        self.rect.y += self.speed
        # если граница экрана => уничтожить
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()
