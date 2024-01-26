import pygame
import sys
from enemy import Enemy
from player import Player
from settings import draw_text, SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.locals import K_SPACE
from leaderboard import Leaderboard


class Game(object):
    def __init__(self, screen, add_enemy):
        # изображение фона
        self.screen = screen
        self.image = pygame.image.load("new_ocean.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # далее
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
        # звуки
        # self.background_music = pygame.mixer.M("dark_music.wav")
        self.change_state_sound = pygame.mixer.Sound("change_screen.wav")
        self.change_state_sound.set_volume(0.1)
        self.player_death_sound = pygame.mixer.Sound("big_ex.wav")
        self.player_death_sound.set_volume(0.1)
        self.enemy_death_sound = pygame.mixer.Sound("small_ex.wav")
        self.enemy_death_sound.set_volume(0.1)
        self.shot_sound = pygame.mixer.Sound("shot.wav")
        self.shot_sound.set_volume(0.05)


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.state == "main menu":
                    if event.key == K_SPACE and len(self.player_name) >= 2:
                        self.change_state_sound.play()
                        self.state = "game"
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    else:
                        if len(self.player_name) < 10 and event.key != pygame.K_SPACE:
                            self.player_name += event.unicode
                if self.state == "game over" and event.key == K_SPACE:
                    self.state = "main menu"
            if event.type == self.ADD_ENEMY:
                enemy = Enemy(self.points)
                self.all_sprites.add(enemy)
                self.enemies.add(enemy)
        if self.state == 'main menu':
            self.main_menu()
        elif self.state == "game":
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_SPACE]:
                self.shot_sound.play()
                self.player.shoot()
            if self.new_game:
                pygame.mixer.music.load("dark_music.wav")
                pygame.mixer.music.set_volume(0.15)
                pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1000)
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
        self.screen.blit(self.image, (0, 0))
        self.all_sprites.update()
        self.enemies.update()
        self.bullets.update()
        for i in self.all_sprites:
            self.screen.blit(i.image, i.rect)
        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            self.shot_sound.stop()
            self.player_death_sound.play()
            self.state = "game over"
            self.leaderboard.insert_update(self.player_name, self.points)
            self.new_game = True
        hits = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        for hit in hits:
            self.shot_sound.stop()
            enemy = Enemy(self.points)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
            self.points += 1
            self.enemy_death_sound.play()
        draw_text('Submarine', self.font, (255, 255, 255), 650, SCREEN_HEIGHT - 40, self.screen)
        draw_text('Ваш счёт: ' + str(self.points), self.font, (255, 255, 255), 20, SCREEN_HEIGHT - 40, self.screen)

    def game_over(self):
        draw_text('ИГРА ОКОНЧЕНА', self.font, (255, 255, 255), 300, 250, self.screen)
        draw_text('Чтобы выйти, нажмите пробел', self.font, (255, 255, 255), 225, 300, self.screen)
