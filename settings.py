def draw_text(text, font, color, x, y, screen):  # текст
    txt = font.render(text, True, color)
    screen.blit(txt, (x, y))


SCREEN_WIDTH = 800  # ширина
SCREEN_HEIGHT = 600  # высота
FPS = 90  # кадры в секунду
