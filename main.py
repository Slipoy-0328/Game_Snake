import pygame
import sys
import random
import pygame_menu
from pygame import *

init()

pygame.init()
SIZE_BLOCK = 20
COUNT_BLOCK_length = 71
COUNT_BLOCK_HEIGHT = 30
MARGIN = 1
HEADER_MARGIN = 70


SNAKE_COLOR = (12, 240, 100)
FRAME_COLOR = (0, 255, 200)
HEADER_COLOR = (0, 204, 153)



RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (125, 249, 255)
win_size = (SIZE_BLOCK * COUNT_BLOCK_length + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK_length,
        SIZE_BLOCK * COUNT_BLOCK_HEIGHT + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK_length + HEADER_MARGIN)
print(win_size)
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Snake")
timer = pygame.time.Clock()
comicsansms = pygame.font.SysFont("comicsansms", 36)
fond = font.SysFont("comicsansms",34)

class SNAKE_BLOCK:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCK_HEIGHT and 0 <= self.y < COUNT_BLOCK_length

    def __eq__(self, other):
        return isinstance(other, SNAKE_BLOCK) and self.x == other.x and self.y == other.y


def DRAW_BLOCK(color, row, column):
    pygame.draw.rect(screen, color, (SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK))

def start_the_game():
    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCK_HEIGHT - 1)
        y = random.randint(0, COUNT_BLOCK_length - 1)
        empty_block = SNAKE_BLOCK(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCK_HEIGHT - 1)
            empty_block.y = random.randint(0, COUNT_BLOCK_length - 1)
        return empty_block

    snake_blocks = [SNAKE_BLOCK(8, 9), SNAKE_BLOCK(9, 9), SNAKE_BLOCK(9, 10)]
    apple = get_random_empty_block()
    d_row = 0
    d_col =  1
    total = 0
    speed = 1

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exit")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_UP or event.key == pygame.K_w) and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == (pygame.K_DOWN or event.key == pygame.K_s) and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == (pygame.K_LEFT or event.key == pygame.K_a) and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == (pygame.K_RIGHT or event.key == pygame.K_d) and d_row != 0:
                    d_row = 0
                    d_col = 1

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, win_size[0], HEADER_MARGIN])

        text_total = comicsansms.render(f"Total {total}", True, WHITE)
        text_speed = comicsansms.render(f"Speed {speed}", True, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK + 400, SIZE_BLOCK))


        for row in range(COUNT_BLOCK_HEIGHT):
            for column in range(COUNT_BLOCK_length):
                if (row + column) % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE
                DRAW_BLOCK(color, row, column)

        head = snake_blocks[-1]
        if not head.is_inside():
            text_crash = comicsansms.render(f"СRASH", True, WHITE)
            screen.blit(text_crash,(765,390))
            print("crash")
            break

        DRAW_BLOCK(RED, apple.x, apple.y)
        for block in snake_blocks:
            DRAW_BLOCK(SNAKE_COLOR, block.x, block.y)

        if apple == head:
            total += 1
            speed = total//5 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()


        new_head = SNAKE_BLOCK(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            print('crash yourself')
            break
        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        pygame.display.flip()
        timer.tick(3+speed)

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
menu.append_option("START", lambda: start_the_game())
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