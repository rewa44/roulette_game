import pygame
import random
from rod import Rod
from roulette import Roulette
from button import Button
from doz import Doz
from doz import Evdd
from spin import Spin
from chips import Chip
from chips import Chip2
from city import City
pygame.init()
pygame.font.init()
by_font = pygame.font.SysFont('Arial', 15)
my_font = pygame.font.SysFont('Arial', 65)
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1200
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
r = 14
g = 104
b = 45
run = True
title = True
gamek = False
rumz = Roulette(0, SCREEN_HEIGHT-406)
balance = 10000
debt = 0
bert = 0
bent = False
rep = Chip(200,50)
rik = Chip2(400,50)
add = False
coords = []
curl = City()
singlez = []
sunken = Spin(850, 50)
payeez = [3,2,2,2,2,3]
rowz = [Rod(675,560-300),Rod(675,620-300),Rod(675,680-300)]
dowz = [Doz(140,745-300),Doz(140+45*4,745-300),Doz(140+45*8,745-300)]
evowz = []
for i in range(6):
    evowz.append(Evdd(140+2*i*45,490,payeez[i]))
for i in range(36):
    singlez.append(i+1)

for i in range(12):
    coords.append((140 + 45 * i, 680-300))
    coords.append((140 + 45 * i, 620-300))
    coords.append((140+45*i, 560-300))

for i in range(36):
    singlez[i] = Button(coords[i][0],coords[i][1])
slunk = Rod(140,740)
for i in range(12):
    rowz[0].fist.append(1 + 3 * i)
    rowz[1].fist.append(2 + 3 * i)
    rowz[2].fist.append(3 + 3 * i)
    dowz[0].fist.append(i+1)
    dowz[1].fist.append(i+13)
    dowz[2].fist.append(i+25)
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
for i in range(18):
    evowz[0].fist.append(i+1)
    evowz[5].fist.append(i+19)
    evowz[1].fist.append(2*(i+1))
    evowz[4].fist.append(2*i+1)
    evowz[2].fist.append(red[i])
    evowz[3].fist.append(black[i])



def spin():
    global balance
    p = random.randint(0,36)
    print(p)
    for item in curl.kist:
        if item[0] == p:
            balance += (item[1] * item[2])
            print("hit!")
    curl.kist = []




disp_bal = my_font.render(str(balance), True, (255, 255, 255))
while run:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if (event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP) and title:
            title = False
            gamek = True
        if event.type == pygame.MOUSEBUTTONUP:
            if rep.rect.collidepoint(pos):
                bert = 100
            if rik.rect.collidepoint(pos):
                bert = 500
            elif sunken.rect.collidepoint(pos) and bert != 0:
                spin()
                disp_bal = my_font.render(str(balance), True, (255, 255, 255))

            for i in range(3):
                if singlez[i].rect.collidepoint(pos):
                    print(i+1)
                    # curl.kist.append([i, bert, 36])
                    # balance -= bert
                    # disp_bal = my_font.render(str(balance), True, (255, 255, 255))
            for i in range(3):
                if rowz[i].rect.collidepoint(pos) and bert != 0:
                    print("rowz" + str(i+1))
                    for m in range(12):
                        curl.kist.append([rowz[i].fist[m],bert,3])
                    balance -= bert
                    disp_bal = my_font.render(str(balance), True, (255, 255, 255))


            for i in range(3):
                if dowz[i].rect.collidepoint(pos):
                    print("dowz" + str(i+1))
                    print(curl.kist)
            for i in range(6):
                if evowz[i].rect.collidepoint(pos):
                    print("evowz" + str(i+1))
    if title:
        screen.fill((r, g, b))
        # add opening image
        pygame.display.update()
    if gamek:
        screen.fill((r, g, b)) # placeholder
        screen.blit(rumz.image, rumz.rect)
        screen.blit(sunken.image, sunken.rect)
        screen.blit(disp_bal, (600,100))
        screen.blit(rep.image, rep.rect)
        screen.blit(rik.image, rik.rect)
        pygame.display.update()
