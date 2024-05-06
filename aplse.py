import pygame
import random
import time
from apple import Apple
from zap import Zap

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 25)
pygame.display.set_caption("Shoot the Fruit!")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


r = 58
g = 120
b = 130

def xcoord_generator():
    funx = random.randint(10, 430)
    return funx

def ycoord_generator():
    funy = random.randint(10,270)
    return funy
start_time = int(time.time())
timer = 0
display_time = my_font.render(str(timer), True, (0, 255, 0))
final_time = 0
display_final = pygame.font.SysFont('Arial', 40).render(str(final_time), True, (100, 255, 0))
# render the text for later
message = "Click the fruit to score!"
display_message = my_font.render(message, True, (255, 255, 255))
clickcount = 0



game_over = "Game Over, You win!"
display_over = pygame.font.SysFont('Arial', 40).render(game_over, True, (255, 255, 255))
game_loser_negative = "NEGATIVE score!! Game over, You lose!"
display_loser_negative = my_font.render(game_loser_negative, True, (200, 200,100))
game_loser_zapple = "You zapped! game over!! you lost."
display_loser_zap = my_font.render(game_loser_zapple, True, (200, 200,100))
# Instantiate the apple
a = Apple(40, 40)
z = Zap(200,200)
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
clickover = False
loser = False
zap = False
restart = False
opened = False
highscored = False
funk = 5
pint = False
f = open("highscore", "r")
data = float(f.readline().strip())
f.close()
display_high = my_font.render(("High score: " + str(data) ), True, (200, 200,100))
# -------- Main Program Loop -----------
while run:
    if not opened:
        f = open("highscore", "r")
        data = float(f.readline().strip())
        opened = True
    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##

    timer = round((time.time() - start_time), 3)

    display_time = my_font.render(str(round(timer)) + "s", True, (0, 255, 0))
    if (timer + 0.5) % 2 == 0:
        z.move(xcoord_generator(), ycoord_generator())
    if (timer +1.5) % 2 == 0:
        z.move(xcoord_generator(), ycoord_generator())
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if z.rect.collidepoint(pos):
                zap = True
            if a.rect.collidepoint(pos):
                a.move(xcoord_generator(), ycoord_generator())
                print(a.x, a.y)
                clickcount += 1
            elif not a.rect.collidepoint(pos):
                clickcount -= 1
                print("bumps")

            if clickcount < 0:
                loser = True
            if clickcount + 1 > funk:
                clickover = True
                final_time = timer
                display_final = pygame.font.SysFont('Arial', 40).render(str(final_time), True, (100, 255, 0))
                if final_time < data:
                    pint = True
                    data = final_time
                    f = open("highscore", "w")
                    f.write(str(data))
                    highscored = True
                    f.close()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("jelo")
            clickover = False
            loser = False
            zap = False
            clickcount = 0
            opened = False
            highscored = False
            start_time = time.time()
    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    if loser:
        screen.fill((r, g, b))
        screen.blit(display_message, (0, 0))
        screen.blit(display_loser_negative, (100,200))
        pygame.display.update()
    elif zap:
        screen.fill((r, g, b))
        screen.blit(display_message, (0, 0))
        screen.blit(display_loser_zap, (50, 200))
        pygame.display.update()
    elif clickover:
        screen.fill((r, g, b))
        screen.blit(display_message, (0, 0))
        screen.blit(display_high, (10, 80))
        screen.blit(display_over, (100, 100))
        screen.blit(display_final, (120, 150))
        screen.blit(my_font.render(str(funk), True, (255, 255, 255)), (10, 40))
        pygame.display.update()
    elif not clickover:
        screen.fill((r, g, b))
        screen.blit(display_high, (10, 80))
        screen.blit(display_message, (0, 0))
        screen.blit(a.image, a.rect)
        screen.blit(z.image, z.rect)
        screen.blit(display_time, (300, 30))
        screen.blit(my_font.render(str(clickcount), True, (255, 255, 255)), (10, 40))
        pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
