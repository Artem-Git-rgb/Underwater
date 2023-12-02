import pygame
import sys
from enemy import Enemy
from player import Player
from settings import draw_text, SCREEN_HEIGHT


class Game(object):
    def __init__(self, screen, add_enemy):
        self.screen = screen
        self.ADD_ENEMY = add_enemy
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Player(self.bullets, self.all_sprites)
        self.all_sprites.add(self.player)
        self.font = pygame.font.Font(None, 36)
        self.points = 0

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == self.ADD_ENEMY:
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
            self.points += 1
        draw_text('Submarine', self.font, (255, 255, 255), 650, SCREEN_HEIGHT - 40, self.screen)
        draw_text('Ваш счёт: ' + str(self.points), self.font, (255, 255, 255), 20, SCREEN_HEIGHT - 40, self.screen)
