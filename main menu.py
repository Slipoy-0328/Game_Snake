from pygame import *

init()

size = (1500, 800)
screen = display.set_mode(size)
display.set_caption("Snake")
img = image.load("завантаження.jpg")
display.set_icon(img)

fond = font.SysFont("comicsansms",34)

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(fond.render(option, True, (0, 255, 25)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0,min(self._current_option_index + direction, len(self._option_surfaces)-1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)

menu = Menu()
menu.append_option("START", lambda: print("START"))
menu.append_option("RECORDS", lambda: print("RECORDS"))
menu.append_option("LEVEL", lambda: print("LEVEL"))
menu.append_option("QUIT", quit)

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_UP or e.key == K_w:
                menu.switch(-1)
            elif e.key == K_DOWN or e.key == K_s:
                menu.switch(1)
            elif e.key == K_SPACE or e.key == K_RETURN:
                menu.select()

    screen.fill((0, 0, 0))

    menu.draw(screen, 700, 100, 75)

    display.flip()
quit()