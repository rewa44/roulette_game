import pygame
import random
from roulette import Roulette
from button import Button
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
for i in range(12):
    coords.append((140+45*i, 560))
    coords.append((140 + 45 * i, 620))
    coords.append((140 + 45 * i, 680))
print(coords)
slunk = Button(185,620,1)
while run:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if (event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP) and title:
            title = False
            gamek = True
        if event.type == pygame.MOUSEBUTTONUP and slunk.rect.collidepoint(pos):
                print("Hit")
    if title:
        screen.fill((r, g, b))
        # add opening image
        pygame.display.update()
    if gamek:
        screen.fill((r+180, g+40, b+20)) # placeholder
        screen.blit(rumz.image, rumz.rect)
        screen.blit(slunk.image, slunk.rect)
        pygame.display.update()