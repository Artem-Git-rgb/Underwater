import sqlite3
import pygame
from settings import draw_text


class Leaderboard:
    def __init__(self, screen):
        self.screen = screen

    with sqlite3.connect("leaderboard.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
            name TEXT NOT NULL,
            score INTEGER DEFAULT 0,
            UNIQUE(name)
        )
        """)

        def insert_update(self, player_name, score):
            with sqlite3.connect("leaderboard.db") as con:
                cur = con.cursor()
                if len(cur.execute("SELECT * FROM leaderboard WHERE name =:Player_name",
                                   {"Player_name": player_name}).fetchall()) == 0:
                    cur.execute("INSERT INTO leaderboard VALUES(:Player_name, :Score)",
                                {"Player_name": player_name, "Score": score})
                else:
                    scr = cur.execute("SELECT * FROM leaderboard WHERE name =:Player_name",
                                      {"Player_name": player_name}).fetchall()
                    if scr[0][0] < score:
                        cur.execute("UPDATE leaderboard SET score =:Score WHERE name =:Player_name",
                                    {"Player_name": player_name, "Score": score})

        def print(self):
            with sqlite3.connect("leaderboard.db") as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM leaderboard ORDER BY score DESC LIMIT 5")
                pos_y = 300
                for r in cur:
                    draw_text(f'Имя: {r[0]}. Очки: {r[1]}', pygame.font.Font(None, 36), (255, 255, 255), 150, pos_y,
                              self.screen)
                    pos_y += 50
