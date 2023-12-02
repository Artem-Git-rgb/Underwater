import pygame
from pygame.locals import (  # назначаю клавиши
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE
)
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, bullets, all_sprites):
        super(Player, self).__init__()
        s_y = 75
        s_x = 25
        self.image = pygame.Surface((s_x, s_y))
        self.rect = self.image.get_rect()
        self.image.fill((250, 250, 250))
        self.rect.x = (SCREEN_WIDTH / 2) - s_x / 2
        self.rect.y = SCREEN_HEIGHT / 2 + s_y
        self.last_shoot = pygame.time.get_ticks()
        self.shoot_speed = 450
        self.all_sprites = all_sprites
        self.bullets = bullets

    def update(self):
        # движение игрока
        pressed_keys = pygame.key.get_pressed()  # проверка на нажатие кнопок
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(4, 0)
        # стрельба
        if pressed_keys[K_SPACE]:
            self.shoot()
        # если граница экрана
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        self.now = pygame.time.get_ticks()
        if self.now - self.last_shoot > self.shoot_speed:
            self.last_shoot = self.now
            bullet = Bullet(self.rect.x + 7, self.rect.y)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((10, 25))
        self.rect = self.image.get_rect()
        self.image.fill((250, 250, 0))
        self.speed = 3
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # движение пули
        self.rect.y -= self.speed
        # если граница экрана => уничтожить
        if self.rect.top < 0:
            self.kill()
