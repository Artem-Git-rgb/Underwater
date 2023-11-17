import pygame
import random
import time
from pygame.locals import (  # назначаю клавиши
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE

)

# основные настройки
pygame.init()
SCREEN_WIDTH = 800  # ширина
SCREEN_HEIGHT = 600  # высота
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
fps = 90  # кадры в секунду


class Game():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            self.all_sprites.update()
            for i in self.all_sprites:
                self.screen.blit(i.image, i.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((20, 20))
        self.rect = pygame.Surface.get_rect(self.image)
        self.image.fill((250, 250, 250))
        self.speed = 1

    def update(self):
        # движение игрока
        self.speed = 0
        pressed_keys = pygame.key.get_pressed()  # проверка на нажатие кнопок
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
        # если граница экрана
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = SCREEN_HEIGHT
        if self.rect.bottom > 0:
            self.rect.bottom = 0


class Enemy():
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((20, 20))
        self.rect = pygame.Surface.get_rect(self.image)
        self.image.fill((255, 10, 10))
        self.rect = self.image.get_rect(
            center=(random.randint(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100), random.randint(0, SCREEN_WIDTH)))
        self.speed = random.randint(5, 7)

    def update(self):
        # движение врага
        self.rect.move_ip(0, self.speed)
        # если граница экрана => уничтожить
        if self.rect.center > SCREEN_HEIGHT:
            self.kill()


# группы
# enemies = pygame.sprite.Group()
# bullets = pygame.sprite.Group()
# счётчик
# time_score = 1
# enemy_score = 0
is_game_over = False
# экран
state = 'game'
# цикл игры
game = Game(screen)
running = True
while running:  # если цикл игры
    clock.tick(fps)  # fps
    screen.fill((0, 50, 120))  # экран
    game.update()  # игра
    pygame.display.flip()
pygame.quit()
