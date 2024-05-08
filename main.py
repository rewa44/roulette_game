import pygame
import random
from rod import Rod
from roulette import Roulette
from button import Button
from doz import Doz
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
ny_font = pygame.font.SysFont('Arial', 45)
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1200
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
r = 58
g = 120
b = 130
run = True
title = True
gamek = False
rumz = Roulette(0, 900-406)
coords = []
singlez = []
rowz = [Rod(675,560),Rod(675,620),Rod(675,680)]
dowz = [Doz(300,300)]
for i in range(36):
    singlez.append(i+1)
print(singlez)
for i in range(12):
    coords.append((140 + 45 * i, 680))
    coords.append((140 + 45 * i, 620))
    coords.append((140+45*i, 560))
print(coords)
for i in range(36):
    singlez[i] = Button(coords[i][0],coords[i][1])
slunk = Rod(140,740)

while run:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if (event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP) and title:
            title = False
            gamek = True
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(36):
                if singlez[i].rect.collidepoint(pos):
                    print(i+1)
            for i in range(3):
                if rowz[i].rect.collidepoint(pos):
                    print("rowz" + str(i+1))
    if title:
        screen.fill((r, g, b))
        # add opening image
        pygame.display.update()
    if gamek:
        screen.fill((r+180, g+40, b+20)) # placeholder
        screen.blit(rumz.image, rumz.rect)
        screen.blit(slunk.image,slunk.rect)
        pygame.display.update()
