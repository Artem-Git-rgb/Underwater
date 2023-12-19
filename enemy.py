import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # изображение
        self.image = pygame.image.load("enemy_image.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (20, 30))
        self.image = pygame.transform.rotate(self.image, 180)
        # далее
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = 0
        self.speed = random.randint(2, 3)

    def update(self):
        # движение врага
        self.rect.y += self.speed
        # если граница экрана => уничтожить
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()
