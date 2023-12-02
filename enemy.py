import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.image.fill((255, 10, 10))
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = 0
        self.speed = random.randint(2, 3)

    def update(self):
        # движение врага
        self.rect.y += self.speed
        # если граница экрана => уничтожить
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()
