import pygame
import random
import time
from fox import Fox
from coin import Coin
from red import Red
from p2 import P2
from spike import Spike


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
ny_font = pygame.font.SysFont('Arial', 45)
pygame.display.set_caption("Coin Collector!")
f = open("highscore", "r")
data = float(f.readline().strip())
f.close()
display_high = ny_font.render(str("high score:" + str(round(data))), True, (255, 200, 100))
# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

name = "Collect coins as fast as you can!"
message = "Collision not detected"
pointsmeter = "100 points obtained! You win. "


r = 50
g = 0
b = 100
timer = 0
# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
display_pfinal = ny_font.render(pointsmeter, True, (255, 255, 255))
display_time = ny_font.render(str(timer), True, (255,255,255))
f = Fox(40, 60)
c = Coin(200, 85)
red = Red(300,20)
spiker = Spike(130,100)
p = P2(100,60)
points = 0
p2points = 0
timelost = False
finaltime = 0
title = True
xtime = []
display_finaltime = ny_font.render(str(finaltime), True, (255, 255, 255))
Welcome = "Welcome to Coin Collector!"
startkey = "Press any key to begin"
final_display_points = ny_font.render(str(points), True, (255, 255, 255))
display_p2final = ny_font.render("player 2 final score was:", True, (255, 255, 255))
display_p2points = ny_font.render(str(p2points), True, (255, 255, 255))
display_welcome = ny_font.render(Welcome, True, (255, 255, 255))
display_startkey = ny_font.render(startkey, True, (255, 255, 255))
start = time.time()
display_points = my_font.render(str(points), True, (255, 255, 255))
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    if not timelost and not title:
        timer = round(10 - (time.time() - start),3)
        display_time = ny_font.render(str(timer), True, (255, 255, 255))
    if (timer + 0.5) % 3 == 0:
        red.set_rand_location()
        spiker.set_rand_location()
    if (timer + 2.5) % 3 == 0:
        red.new_loc(10000,10000)
        spiker.set_rand_location()
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        f.move_direction("right")
    if keys[pygame.K_a]:
        f.move_direction("left")
    if keys[pygame.K_w]:
        f.move_direction("up")
    if keys[pygame.K_s]:
        f.move_direction("down")

    if keys[pygame.K_RIGHT]:
        p.move_direction("right")
    if keys[pygame.K_LEFT]:
        p.move_direction("left")
    if keys[pygame.K_UP]:
        p.move_direction("up")
    if keys[pygame.K_DOWN]:
        p.move_direction("down")
    # collision
    if f.rect.colliderect(red.rect):
        red.new_loc(10000,10000)
        points += 15
        display_points = my_font.render(str(points), True, (255, 255, 255))
    if f.rect.colliderect(spiker.rect):
        spiker.set_rand_location()
        points -= 10
        display_points = my_font.render(str(points), True, (255, 255, 255))
    if f.rect.colliderect(c.rect):
        message = "Collision detected"
        display_message = my_font.render(message, True, (255, 255, 255))
        c.set_location(random.randint(0,500), random.randint(0,340),)
        points += 10
        display_points = my_font.render(str(points), True, (255, 255, 255))
    ## player 2
    if p.rect.colliderect(red.rect):
        red.new_loc(10000,10000)
        p2points += 15
        display_p2points = ny_font.render(str(p2points), True, (255, 255, 255))
    if p.rect.colliderect(spiker.rect):
        spiker.set_rand_location()
        p2points -= 10
        display_p2points = ny_font.render(str(p2points), True, (255, 255, 255))
    if p.rect.colliderect(c.rect):
        message = "Collision detected"
        display_message = ny_font.render(message, True, (255, 255, 255))
        c.set_location(random.randint(0,500), random.randint(0,340),)
        p2points += 10
        display_p2points = ny_font.render(str(p2points), True, (255, 255, 255))

    if not title and timer <= 0:
        timelost = True
        finaltime = "0.000"
        display_finaltime = ny_font.render(str(finaltime), True, (255, 255, 255))
        display_pfinal = ny_font.render("player 1 final score was:", True, (255, 255, 255))
        final_display_points = ny_font.render(str(points), True, (255, 255, 255))
        f.x = 2000
        f.y = 2000
        p.x = 2000
        p.y = 2000
        if points > data:
            fa = open("highscore", "w")
            fa.write(str(points))
            fa.close()
            display_high = ny_font.render(str("high score:" + str(round(points))), True, (255, 200, 100))
        display_p2final = ny_font.render("player 2 final score was:", True, (255, 255, 255))
        final_display_p2points = ny_font.render(str(p2points), True, (255, 255, 255))
        if p2points > data:
            fa = open("highscore", "w")
            fa.write(str(points))
            fa.close()
            display_high = ny_font.render(str("high score:" + str(round(points))), True, (255, 200, 100))

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.KEYUP and title:
            title = False
            start = time.time()




    if title:
        screen.fill((r, g, b))
        screen.blit(display_welcome, (20,20))
        screen.blit(display_startkey, (20, 70))
        screen.blit(f.image, (200,200))
        screen.blit(f.image, (300,200))
        screen.blit(p.image, (50, 200))
        screen.blit(c.image, (500,0))
        screen.blit(c.image, (0,340))
        screen.blit(c.image, (500,340))
        screen.blit(c.image, (0,0))
        screen.blit(display_high, (150, 320))
        pygame.display.update()
    elif timelost:
        screen.fill((r, g, b))
        screen.blit(display_high, (200,20))
        screen.blit(display_name, (0, 0))
        screen.blit(display_finaltime, (0, 50))
        screen.blit(display_pfinal, (30, 100))
        screen.blit(final_display_points, (50, 145))
        screen.blit(display_p2final, (30, 235))
        screen.blit(display_p2points, (100, 320))
        pygame.display.update()
    else:
        screen.fill((r, g, b))
        screen.blit(display_name, (0, 0))
        screen.blit(f.image, f.rect)
        screen.blit(p.image, p.rect)
        screen.blit(display_time, (0, 50))
        screen.blit(c.image, c.rect)
        screen.blit(display_points, (0, 30))
        screen.blit(display_p2points, (400, 30))
        screen.blit(red.image, red.rect)
        screen.blit(spiker.image, spiker.rect)
        pygame.display.update()
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()



