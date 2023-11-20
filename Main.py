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
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, random.randrange(400, 500))


class Game():
    def __init__(self, screen, add_enemy):
        self.screen = screen
        self.player = Player()
        self.ADD_ENEMY = add_enemy
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.enemies = pygame.sprite.Group()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == ADD_ENEMY:
                enemy = Enemy()
                self.enemies.add(enemy)
                self.all_sprites.add(enemy)
        self.all_sprites.update()
        self.enemies.update()
        for i in self.all_sprites:
            self.screen.blit(i.image, i.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        s_y = 60
        s_x = 25
        self.image = pygame.Surface((s_x, s_y))
        self.rect = self.image.get_rect()
        self.image.fill((250, 250, 250))
        self.rect.x = (SCREEN_WIDTH / 2) - s_x / 2
        self.rect.y = SCREEN_HEIGHT / 2 - s_y / 2

    def update(self):
        # движение игрока
        pressed_keys = pygame.key.get_pressed()  # проверка на нажатие кнопок
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        # если граница экрана
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


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


# счётчик
# time_score = 1
# enemy_score = 0
is_game_over = False
# экран
state = 'game'
# цикл игры
game = Game(screen, ADD_ENEMY)
running = True
while running:  # если цикл игры
    clock.tick(fps)  # fps
    screen.fill((0, 50, 120))  # экран
    game.update()  # игра
    pygame.display.flip()
pygame.quit()
