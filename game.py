import pygame
import sys
from enemy import Enemy
from player import Player
from settings import draw_text, SCREEN_HEIGHT
from pygame.locals import K_SPACE
from leaderboard import Leaderboard


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
        self.state = "main menu"
        self.new_game = True
        # таблица рекордов
        self.player_name = ""
        self.leaderboard = Leaderboard(screen)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.state == "main menu":
                    if event.key == K_SPACE and len(self.player_name) >= 2:
                        self.state = "game"
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    else:
                        if len(self.player_name) < 10 and event.key != pygame.K_SPACE:
                            self.player_name += event.unicode
                if self.state == "game over" and event.key == K_SPACE:
                    self.state = "main menu"
            if event.type == self.ADD_ENEMY:
                enemy = Enemy()
                self.all_sprites.add(enemy)
                self.enemies.add(enemy)
        if self.state == 'main menu':
            self.main_menu()
        elif self.state == "game":
            if self.new_game:
                self.all_sprites = pygame.sprite.Group()
                self.enemies = pygame.sprite.Group()
                self.bullets = pygame.sprite.Group()
                self.player = Player(self.bullets, self.all_sprites)
                self.all_sprites.add(self.player)
                self.points = 0
                self.new_game = False
            self.game()
        else:
            self.game_over()

    def main_menu(self):
        draw_text('Submarine', self.font, (255, 255, 255), 330, 100, self.screen)
        draw_text('Уклоняйся от ракет и выпускай пули', self.font, (255, 255, 255), 190, 150, self.screen)
        draw_text('Стрелочки - движение, пробел - выстрел', self.font, (255, 255, 255), 170, 200, self.screen)
        draw_text('Таблица рекордов:', self.font, (255, 255, 255), 150, 250, self.screen)
        draw_text('Введите имя: ', self.font, (255, 255, 255), 450, 250, self.screen)
        draw_text(self.player_name, self.font, (255, 255, 255), 500, 350, self.screen)
        self.leaderboard.print()

    def game(self):
        self.all_sprites.update()
        self.enemies.update()
        self.bullets.update()
        for i in self.all_sprites:
            self.screen.blit(i.image, i.rect)
        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            self.state = "game over"
            self.leaderboard.insert_update(self.player_name, self.points)
            self.new_game = True
        hits = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        for hit in hits:
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
            self.points += 1
        draw_text('Submarine', self.font, (255, 255, 255), 650, SCREEN_HEIGHT - 40, self.screen)
        draw_text('Ваш счёт: ' + str(self.points), self.font, (255, 255, 255), 20, SCREEN_HEIGHT - 40, self.screen)

    def game_over(self):
        draw_text('ИГРА ОКОНЧЕНА', self.font, (255, 255, 255), 300, 250, self.screen)
        draw_text('Чтобы выйти, нажмите пробел', self.font, (255, 255, 255), 225, 300, self.screen)
