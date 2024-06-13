import pygame
import math
import random
import time
imparted = ["Rod", "Roulette", "Button", "Doz"]
from rod import *
import os

pygame.init()
pygame.font.init()
by_font = pygame.font.SysFont('Arial', 15)
my_font = pygame.font.SysFont('Arial', 55)
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
w = Wheel(820,250)
bud = Ball(890,300)
run = True
title = True
gamek = False
rumz = Roulette(0, SCREEN_HEIGHT-406)
balance = 10000
debt = 0
bert = 0
bent = False
rep = Chip(0,0)
rik = Chip2(150,0)
ros = Chip3(300,0)
add = False
coords = []
curl = City()
singlez = []
sunken = Spin(850, 50)
payeez = [3,2,2,2,2,3]
rowz = [Rod(675,680-300),Rod(675,620-300),Rod(675,560-300)]
dowz = [Doz(140,745-300),Doz(140+45*4,745-300),Doz(140+45*8,745-300)]
evowz = []
disp_bank = my_font.render(str("no more money! You lose!"), True, (255, 255, 255))
tum = Title(0,0)
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
disp_put = my_font.render(str("bet amount: " + str(put)), True, (255, 255, 255))
hello = ""
disp_hello = my_font.render(str(hello), True, (255, 255, 255))
# disp_barf = my_font.render(str("hello"), True, (255, 255, 255))
disp_belt = my_font.render(str("points:"), True, (255, 255, 255))
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
    # disp_barf = my_font.render(str(p), True, (255, 255, 255))
    hello = "You lose!"
    for item in curl.kist:
        if item[0] == p:
            balance += (item[1] * item[2])
            print("hit!")
            hello = "You win!"
    disp_hello = my_font.render(str(hello), True, (255, 255, 255))

    put = 0
    disp_put = my_font.render(str("bet amount: " + str(put)), True, (255, 255, 255))
    bert = 0
    curl.kist = []
highway = [0,32,15,19,4,
           21,2,25,17,34,
           6,27,13,36,11,
           30,8,23,10,5,
           24,16,33,1,20,
           14,31,9,22,18,
           29,7,28,12,35,
           3,26]
ket = 360/37
pitt = 3232323232
play = False
def move():
    frame = 0 #
    global pitt
    global play
    pitt = 32030
    clock = pygame.time.Clock() #
    yes = True
    global angle
    perk = round(random.uniform(4, 7.23),2)
    global disp_hello
    while yes:
        bud.x = 120 * math.cos(math.radians(angle)) + w.x + (612/4) - 30/2 + 5
        bud.y = 120 * math.sin(math.radians(angle)) + w.y + (612/4) - 30/2 + 5
        bud.rect = pygame.Rect(bud.x, bud.y, bud.image_size[0] * 0.1, bud.image_size[1] * 0.1)
        print(bud.x)
        print(bud.y)
        clock.tick(400)
        frame += 10
        if frame % 20 == 0:
            angle += perk
            print("money   " + str(frame))
        if angle >= 360:
            angle = 0
        print("whats up    " + str(perk))
        print("hello   " + str(angle))
        print("swag like us " + str(round(angle / ket)))
        perk *= 0.9985
        screen.fill((r, g, b))
        screen.blit(rumz.image, rumz.rect)
        screen.blit(sunken.image, sunken.rect)
        screen.blit(disp_bal, (300, 160))
        screen.blit(rep.image, rep.rect)
        screen.blit(rik.image, rik.rect)
        screen.blit(ros.image, ros.rect)
        screen.blit(disp_belt, (100, 160))
        screen.blit(disp_put, (460, 10))
        screen.blit(disp_hello, (460, 70))
        # screen.blit(disp_barf, (750, 400))
        screen.blit(w.image, w.rect)
        screen.blit(bud.image, bud.rect)
        pygame.display.update()
        if perk < 0.2:
            break
    for i in range(37):
        if (360 / 37) * i < angle < (360 / 37) * (i + 1):
            pitt = highway[i]
            print(highway[i])
            print(angle / ket)
    screen.fill((r, g, b))
    screen.blit(rumz.image, rumz.rect)
    screen.blit(sunken.image, sunken.rect)
    screen.blit(disp_bal, (300, 160))
    screen.blit(rep.image, rep.rect)
    screen.blit(rik.image, rik.rect)
    screen.blit(ros.image, ros.rect)
    screen.blit(disp_belt, (100, 160))
    screen.blit(disp_put, (460, 10))
    screen.blit(disp_hello, (460, 70))
    # screen.blit(disp_barf, (750, 400))
    screen.blit(w.image, w.rect)
    screen.blit(bud.image, bud.rect)
    pygame.display.update()
    disp_hello = my_font.render(str(highway[int(angle // ket)]), True, (255, 255, 255))
    pitt = highway[int(round(angle / ket))]
    play = False
    return pitt


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
                bert = 1000
            elif ros.rect.collidepoint(pos):
                bert = 10000
            elif sunken.rect.collidepoint(pos) and bert != 0 \
                    and disp_hello != my_font.render(str("spinning..."), True, (255, 255, 255)):
                if curl.kist == []:
                    disp_hello = my_font.render(str("place a bet first!"), True, (255, 255, 255))
                else:
                    disp_hello = my_font.render(str("spinning..."), True, (255, 255, 255))
                    play = True
                    pitt = move()
                    for item in curl.kist:
                        if item[0] == pitt:
                            balance += (item[1] * item[2])
                            print("hit!")
                            hello = str(pitt) + ", You win!"
                    if hello != str(pitt) + ", You win!":
                        hello = str(pitt) + ", You lose!"
                    put = 0
                    disp_put = my_font.render(str("bet amount: " + str(put)), True, (255, 255, 255))
                    disp_hello = my_font.render(str(hello), True, (255, 255, 255))
                    disp_bal = my_font.render(str(balance), True, (255, 255, 255))
                    curl.kist = []

            for i in range(36):
                if singlez[i].rect.collidepoint(pos) and \
                        disp_hello != my_font.render(str("spinning..."), True, (255, 255, 255)):
                    if balance == 0:
                        disp_hello = my_font.render(str("no money to bet!"), True, (255, 255, 255))
                    else:
                        print("sing" + str(i + 1))
                        curl.kist.append([i + 1, bert, 36])
                        balance -= bert
                        put += bert
                        disp_bal = my_font.render(str(balance), True, (255, 255, 255))
                        disp_put = my_font.render(str("bet amount: " + str(put)), True, (255, 255, 255))

            for i in range(3):

                if rowz[i].rect.collidepoint(pos) and bert != 0 and disp_hello != my_font.render(str("spinning..."), True, (255, 255, 255)):
                    if balance == 0:
                        disp_hello = my_font.render(str("no money to bet!"), True, (255, 255, 255))
                    else:
                        print("rowz" + str(i + 1))
                        for m in range(12):
                            curl.kist.append([rowz[i].fist[m], bert, 3])
                        balance -= bert
                        put += bert
                        disp_bal = my_font.render(str(balance), True, (255, 255, 255))
                        disp_put = my_font.render(str("bet amount: " + str(put)), True, (255, 255, 255))



            for i in range(3):
                if dowz[i].rect.collidepoint(pos) and disp_hello != my_font.render(str("spinning..."), True, (255, 255, 255)):

                    if balance == 0:
                        disp_hello = my_font.render(str("no money to bet!"), True, (255, 255, 255))
                    else:
                        print("dowz" + str(i + 1))
                        for m in range(12):
                            curl.kist.append([dowz[i].fist[m], bert, 3])
                        balance -= bert
                        put += bert
                        disp_bal = my_font.render(str(balance), True, (255, 255, 255))
                        disp_put = my_font.render(str("bet amount: " + str(put)), True, (255, 255, 255))
            for i in range(6):

                if evowz[i].rect.collidepoint(pos) and disp_hello != my_font.render(str("spinning..."), True, (255, 255, 255)):
                    if balance == 0:
                        disp_hello = my_font.render(str("no money to bet!"), True, (255, 255, 255))
                    else:
                        print("evowz" + str(i + 1))
                        for m in range(18):
                            curl.kist.append([evowz[i].fist[m], bert, 2])
                        balance -= bert
                        put += bert
                        disp_bal = my_font.render(str(balance), True, (255, 255, 255))
                        disp_put = my_font.render(str("bet amount: " + str(put)), True, (255, 255, 255))
    if balance <= 0 and not play and put == 0:
        time.sleep(3)
        gamek = False
        balance = 0
        screen.fill((r, g, b))
        screen.blit(disp_bank, (300,300))
        pygame.display.update()
    if title:
        screen.fill((r, g, b))
        screen.blit(tum.image,tum.rect)
        pygame.display.update()
    if gamek:
        screen.fill((r, g, b))
        screen.blit(rumz.image, rumz.rect)
        screen.blit(sunken.image, sunken.rect)
        screen.blit(disp_bal, (300,160))
        screen.blit(rep.image, rep.rect)
        screen.blit(rik.image, rik.rect)
        screen.blit(ros.image, ros.rect)
        screen.blit(disp_belt, (100,160))
        screen.blit(disp_put, (460,10))
        screen.blit(disp_hello, (460,70))
        # screen.blit(disp_barf, (750,400))
        screen.blit(w.image, w.rect)
        screen.blit(bud.image, bud.rect)
        pygame.display.update()
