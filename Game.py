import pygame
pygame.init()
size = (1500,800)
size_snake = (1430,730)
come_backx = False
come_backy = False
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
img = pygame.image.load("завантаження.jpg")
pygame.display.set_icon(img)

fond = pygame.font.SysFont("comicsansms",64)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
follow = fond.render("Hello", 1, GREEN, BLACK)
follow_snake = fond.render("    ", 1, BLACK, GREEN)
x, y = 0, -20
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(follow, (700, 400))
    screen.blit(follow_snake, (x, y))
    if come_backx == False:
        x+=1
    elif x == 0 and y <= 720:
        x == 0
    else:
        x-=1
    if come_backy == False:
        y ==0
    else:
        y-=1
    if x >= 1430:
        x = 1430
        y+=1
    if y >= 720:
        y == 720
        come_backx = True
        if x==0:

            come_backy = True


    pygame.display.update()

screen = pygame.display.set_mode(size)
