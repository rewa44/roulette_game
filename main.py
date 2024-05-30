import pygame
import math
import random
import time
from rod import Rod
from roulette import Roulette
from button import Button
from doz import Doz
from doz import Evdd
from spin import Spin
from chips import Chip
from chips import Chip2
from chips import Chip3
from city import City
import os
from proto import Wheel
from proto import Ball
pygame.init()
pygame.font.init()
by_font = pygame.font.SysFont('Arial', 15)
my_font = pygame.font.SysFont('Arial', 65)
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1200
size = (SCREEN_WIDTH - 10, SCREEN_HEIGHT - 50)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
r = 14
g = 104
b = 45
w = Wheel(890,300)
bud = Ball(890,300)
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
ros = Chip3(600,50)
add = False
coords = []
curl = City()
singlez = []
sunken = Spin(850, 50)
payeez = [3,2,2,2,2,3]
rowz = [Rod(675,680-300),Rod(675,620-300),Rod(675,560-300)]
dowz = [Doz(140,745-300),Doz(140+45*4,745-300),Doz(140+45*8,745-300)]
evowz = []
for i in range(6):
    evowz.append(Evdd(140+2*i*45,490,payeez[i]))
for i in range(36):
    singlez.append(i+1)

for i in range(12):
    coords.append((140 + 45 * i, 680 - 300))
    coords.append((140 + 45 * i, 620 - 300))
    coords.append((140 + 45 * i, 560 - 300))

angle = 0

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

put = 0
disp_put = my_font.render(str(put), True, (255, 255, 255))
hello = ""
disp_hello = my_font.render(str(hello), True, (255, 255, 255))
disp_barf = my_font.render(str("hello"), True, (255, 255, 255))
def spin():
    global balance
    global disp_put
    global put
    global bert
    global disp_hello
    global hello
    global disp_barf
    p = random.randint(0,36)
    # p = 23
    print(p)
    disp_hello = my_font.render(str("spinning..."), True, (255, 255, 255))
    # time.sleep(3)
    disp_barf = my_font.render(str(p), True, (255, 255, 255))
    hello = "You lose!"
    for item in curl.kist:
        if item[0] == p:
            balance += (item[1] * item[2])
            print("hit!")
            hello = "You win!"
    disp_hello = my_font.render(str(hello), True, (255, 255, 255))

    put = 0
    disp_put = my_font.render(str(put), True, (255, 255, 255))
    bert = 0
    curl.kist = []
highway = [0,32,15,19,4,21,2,25,17,3,4,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,26]
ket = 360/37
def move():
    frame = 0 #
    clock = pygame.time.Clock() #
    yes = True
    global angle
    perk = random.randint(4,7) + random.randint(0,9) * 0.1 + random.randint(0,9) * 0.01
    global disp_hello
    while yes:
        bud.x = 120 * math.cos(math.radians(angle)) + 900
        bud.y = 120 * math.sin(math.radians(angle)) + 350
        bud.rect = pygame.Rect(bud.x, bud.y, bud.image_size[0] * 0.1, bud.image_size[1] * 0.1)
        screen.fill((r, g, b))  # placeholder
        screen.blit(rumz.image, rumz.rect)
        screen.blit(sunken.image, sunken.rect)
        screen.blit(disp_bal, (800, 350))
        screen.blit(rep.image, rep.rect)
        screen.blit(rik.image, rik.rect)
        screen.blit(ros.image, ros.rect)
        screen.blit(disp_put, (300, 160))
        screen.blit(disp_hello, (800, 300))
        screen.blit(disp_barf, (750, 400))
        screen.blit(w.image, w.rect)
        screen.blit(bud.image, bud.rect)
        pygame.display.update()
        print(bud.x)
        print(bud.y)
        clock.tick(400)
        frame += 10
        if frame % 20 == 0:
            angle += perk
            print("money   " + str(frame))
        if angle > 360:
            angle = 0
        print("whats up    " + str(perk))
        print("hello   " + str(angle))
        print(str(int(angle // ket)))
        perk *= 0.9985
        if perk < 0.2:
            break

    disp_hello = my_font.render(str(highway[int(angle // ket)]), True, (255, 255, 255))
    return highway[int(angle // ket)]

def test():
    frame = 0
    clock = pygame.time.Clock()
    yes = True
    angle = random.randint(0,359)
    perk = random.uniform(4.7, 6.2)
    while yes:
        clock.tick(120)
        bud.x = 120 * math.cos(math.radians(angle)) + 300
        bud.y = 120 * math.sin(math.radians(angle)) + 150
        if frame % 60 == 0:
            angle += perk
        if angle > 360:
            angle = 0
        print(perk)
        print("hello   " + str(angle))
        print(str(int(angle // ket)))
        perk *= 0.9985
        if perk < 0.2:
            break

    return str( str(highway[int(angle // ket)]))


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
            elif rik.rect.collidepoint(pos):
                bert = 500
            elif ros.rect.collidepoint(pos):
                bert = 1000
            elif sunken.rect.collidepoint(pos) and bert != 0:
                disp_hello = my_font.render(str("spinning..."), True, (255, 255, 255))
                print(move())
                disp_bal = my_font.render(str(balance), True, (255, 255, 255))


            for i in range(36):
                if singlez[i].rect.collidepoint(pos):
                    print("sing" + str(i+1))
                    curl.kist.append([i+1, bert, 36])
                    balance -= bert
                    put += bert
                    disp_bal = my_font.render(str(balance), True, (255, 255, 255))
                    disp_put = my_font.render(str(put), True, (255, 255, 255))
            for i in range(3):
                if rowz[i].rect.collidepoint(pos) and bert != 0:
                    print("rowz" + str(i+1))
                    for m in range(12):
                        curl.kist.append([rowz[i].fist[m],bert,3])
                    balance -= bert
                    put += bert
                    disp_bal = my_font.render(str(balance), True, (255, 255, 255))
                    disp_put = my_font.render(str(put), True, (255, 255, 255))



            for i in range(3):
                if dowz[i].rect.collidepoint(pos):
                    print("dowz" + str(i+1))
                    for m in range(12):
                        curl.kist.append([dowz[i].fist[m], bert, 3])
                    balance -= bert
                    put += bert
                    disp_bal = my_font.render(str(balance), True, (255, 255, 255))
                    disp_put = my_font.render(str(put), True, (255, 255, 255))
            for i in range(6):
                if evowz[i].rect.collidepoint(pos):
                    print("evowz" + str(i+1))
                    for m in range(18):
                        curl.kist.append([evowz[i].fist[m], bert, 2])
                    balance -= bert
                    put += bert
                    disp_bal = my_font.render(str(balance), True, (255, 255, 255))
                    disp_put = my_font.render(str(put), True, (255, 255, 255))
    if title:
        screen.fill((r, g, b))
        # add opening image
        pygame.display.update()
    if gamek:
        screen.fill((r, g, b)) # placeholder
        screen.blit(rumz.image, rumz.rect)
        screen.blit(sunken.image, sunken.rect)
        screen.blit(disp_bal, (800,350))
        screen.blit(rep.image, rep.rect)
        screen.blit(rik.image, rik.rect)
        screen.blit(ros.image, ros.rect)
        screen.blit(disp_put, (300,160))
        screen.blit(disp_hello, (800,300))
        screen.blit(disp_barf, (750,400))
        screen.blit(w.image, w.rect)
        screen.blit(bud.image, bud.rect)
        pygame.display.update()
