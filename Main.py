import pygame
import random
import time
import sys
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


# текст
def draw_text(text, font, color, x, y, screen):
    txt = font.render(text, True, color)
    screen.blit(txt, (x, y))


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
        self.ADD_ENEMY = add_enemy
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Player(self.bullets, self.all_sprites)
        self.all_sprites.add(self.player)
        self.font = pygame.font.Font(None, 36)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ADD_ENEMY:
                enemy = Enemy()
                self.all_sprites.add(enemy)
                self.enemies.add(enemy)
        self.all_sprites.update()
        self.enemies.update()
        self.bullets.update()
        for i in self.all_sprites:
            self.screen.blit(i.image, i.rect)
        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            pygame.quit()
            sys.exit()
        hits = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        for hit in hits:
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
        draw_text('Submarine', self.font, (255, 255, 255), 20, SCREEN_HEIGHT - 40, self.screen)


class Player(pygame.sprite.Sprite):
    def __init__(self, bullets, all_sprites):
        super(Player, self).__init__()
        s_y = 75
        s_x = 25
        self.image = pygame.Surface((s_x, s_y))
        self.rect = self.image.get_rect()
        self.image.fill((250, 250, 250))
        self.rect.x = (SCREEN_WIDTH / 2) - s_x / 2
        self.rect.y = SCREEN_HEIGHT / 2 - s_y / 2
        self.last_shoot = pygame.time.get_ticks()
        self.shoot_speed = 500
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
# экран
state = 'game'
# цикл игры
game = Game(screen, ADD_ENEMY)
while True:  # если цикл игры
    clock.tick(fps)  # fps
    screen.fill((0, 50, 120))  # экран
    game.update()  # игра
    pygame.display.flip()
