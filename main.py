import pygame
import random
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
ny_font = pygame.font.SysFont('Arial', 45)
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
r = 58
g = 120
b = 130
run = True
title = True
gamek = False
while run:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if (event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP) and title:
            title = False
            gamek  = True

    if title:
        screen.fill((r, g, b))
        # add opening image
        pygame.display.update()
   if gamek:
        screen.fill((r+180, g+40, b+20))
        # add opening image
        pygame.display.update()
